from time import sleep
from datetime import datetime
from itertools import chain
import logging
import json
import time
import iso8601

from typing import Any, Dict, List, Optional
import requests

from output import Output, KafkaOutput, TerminalOutput, FileOutput, InfluxOutput


class NaiadesClient():
    verbose: int
    configuration_path: str
    production_mode: bool

    # API Server
    ip: str
    port: str
    fiware_service: str
    entity_id: str
    required_attributes: List[str]
    output_attributes_names: List[str]
    output_timestamp_name: str
    output_timestamp_format: str
    base_url: str
    headers: Dict[str, str]
    
    last_timestamp: str

    # TIMING
    seconds_between_samples: int
    second_in_minute: str
    minute_in_hour: str
    hour_in_day: str
    period: int

    outputs: List["Output"]
    output_configurations: List[Dict[Any, Any]]

    def __init__(self, configurationPath: str = None) -> None:
        self.configuration(configurationPath=configurationPath)

    def configuration(self, configurationPath: str = None) -> None:
        self.configuration_path = configurationPath

        # Read config file
        with open(configurationPath) as data_file:
            conf = json.load(data_file)

        if("verbose" in conf):
            self.verbose = conf["verbose"]
        else:
            self.verbose = 0
        
        if("production_mode" in conf):
            self.production_mode = conf["production_mode"]
        else:
            self.production_mode = False

        # API SERVER CONFIGURATION
        self.ip = conf["ip"]
        self.port = conf["port"]
        self.fiware_service = conf["fiware_service"]
        self.entity_id = conf["entity_id"]
        self.required_attributes = conf["required_attributes"]
        
        # Makes shure that some required attributes are specified
        assert len(self.required_attributes) > 0, "Required attributes must be specified"

        # Base url construction
        self.base_url = "http://" + self.ip + ":" + self.port +\
                        "/v2/entities/" + self.entity_id + "?attrs=" +\
                        self.required_attributes[0]
        # Adding attributes parameter
        for a in self.required_attributes[1:]:
            self.base_url = self.base_url + "," + a

        # Headers construction
        self.headers = {
            "Fiware-Service": self.fiware_service,
            "Fiware-ServicePath": "/",
            "Content-Type": "application/json"
        }

        # The from field in configuration file must contain
        # SO8601 format (e.g., 2018-01-05T15:44:34)
        if("from" in conf):
            self.last_timestamp = conf["from"]
        else:
            self.last_timestamp = None

        # TIMING CONFIGURATION
        if("period" in conf):
            self.period = conf["period"]
        else:
            self.period = None
        self.seconds_between_samples = None
        self.second_in_minute = None
        self.minute_in_hour = None
        self.hour_in_day = None
        if("seconds_between_samples" in conf):
            self.seconds_between_samples = conf["seconds_between_samples"]
        elif("second_in_minute" in conf):
            self.second_in_minute = conf["second_in_minute"]
        elif("minute_in_hour" in conf):
            self.minute_in_hour = conf["minute_in_hour"]
        elif("hour_in_day" in conf):
            self.hour_in_day = conf["hour_in_day"]

        # OUTPUT CONFIGURATION
        # If config file contains output_timestamp_name set it from there,
        # otherwise set it to timestamp
        if("output_timestamp_name" in conf):
            self.output_timestamp_name = conf["output_timestamp_name"]
        else:
            self.output_timestamp_name = "timestamp"
        # If config file contains output_timestamp_format set it from there,
        # otherwise set it to iso8601
        if("output_timestamp_format" in conf):
            self.output_timestamp_format = conf["output_timestamp_format"]
        else:
            self.output_timestamp_format = "iso8601"
        # If config file contains output_attributes_names set it from there,
        # otherwise use required_attributes
        if("output_attributes_names" in conf):
            self.output_attributes_names = conf["output_attributes_names"]
        else:
            self.output_attributes_names = self.required_attributes

        # Initialize and configure outputs
        self.outputs = [eval(o) for o in conf["outputs"]]
        output_configurations = conf["output_configurations"]
        #construct field names
        field_names = [self.output_timestamp_name]
        for a in self.output_attributes_names:
            if(isinstance(a, list)):
                field_names = field_names + a
            else:
                field_names.append(a)
        for o in range(len(self.outputs)):
            output_configurations[o]["field_names"] = field_names
            # Add output_timestamp_name to output's configuration (for influx output)
            output_configurations[o]["output_timestamp_name"] = self.output_timestamp_name
            self.outputs[o].configure(output_configurations[o])

    def obtain(self) -> None:
        # A method that obtains data (since last timestamp if specified)
        # from API

        # Print message if required
        if(self.verbose == 1):
            print("{}: Obtaining {}.".format(datetime.now(), self.entity_id))

        # If last timestamp is not None add it to the url parameters
        if(self.last_timestamp is not None):
            url = self.base_url + "&fromDate=" + self.last_timestamp
        else:
            url = self.base_url

        # Send the get request
        try:
            r = requests.get(url, headers=self.headers)
        except requests.exceptions.RequestException as e:  # This is the correct syntax
            logging.warning(e)
        else:
            logging.info('Successfuly obtained from API ' + time.ctime())

            # If status code is not 200 raise an error
            if(r.status_code != requests.codes.ok):
                print("Data from {} could not be obtained. Error code: {}.".format(self.entity_id, r.status_code))
                return

            # Retrieve attributest and timestamps from body of response
            body = r.json()
            attributes = body["attributes"]
            timestamps = body["index"]

            number_of_samples = len(timestamps)
            # Required to see if request needs to be repeated
            total_samples_obtained = len(timestamps)

            # if there is at least one sample
            if(number_of_samples > 0):

                # Remove last_timestamp timestamps
                remove = 0
                while(timestamps[remove] == self.last_timestamp):
                    remove += 1
                    if(remove >= number_of_samples):
                        return
                number_of_samples -= remove
                timestamps = timestamps[remove:]
                for a in attributes:
                    a["values"] = a["values"][remove:]

                # Creates a dictionary with attribute names for keys and arrays of
                # values for values
                attributers_dict = {}
                for a in attributes:
                    attributers_dict[a["attrName"]] = a["values"]

                # For every sample send out a dictionary with the data
                for sample in range(number_of_samples):
                    # Create a dictionary to ba outputted and add attributes to it
                    # with defined names

                    # Transforms timestamp to specified format if needed
                    if(self.output_timestamp_format == "iso8601"):
                        t = timestamps[sample]
                    elif(self.output_timestamp_format == "unix_time"):
                        t = self.iso8601ToUnix(timestamps[sample])
                    else:
                        print("Output timestamp format not supported")
                        exit(1)

                    # Loops over required attributes and adds them to the
                    # output_dict
                    output_dict = {self.output_timestamp_name: t}
                    for i in range(len(self.required_attributes)):
                        output_attribute_name = self.output_attributes_names[i]
                        attribute = attributers_dict[self.required_attributes[i]][sample]
                        # If output_attribute_name is a list that means that 
                        # attribute is also a list and elements of the list are
                        # added to the output_dict.
                        if(isinstance(output_attribute_name, list)):
                            if(not isinstance(attribute, list)):
                                print("Warrning: Obtained attribute {} is supposed to be a list (it will be replaced with None values).".format(attribute))
                                attribute = [None] * len(output_attribute_name)
                            elif(len(attribute) < len(output_attribute_name)):
                                print("Warrning: Obtained attribute {} is supposed to be of length {} but is not. None values will be added.".format(attribute, len(output_attribute_name)))
                                while(len(attribute) < len(output_attribute_name)):
                                    attribute.append(None)
                            elif(len(attribute) > len(output_attribute_name)):
                                print("Warrning: Obtained attribute {} is supposed to be of shape {} but is not. None value will be used instead.".format(attribute, output_attribute_name))
                                attribute = [None] * len(output_attribute_name)
                            for name_idx in range(len(output_attribute_name)):
                                name = output_attribute_name[name_idx]
                                attribute_value = attribute[name_idx]
                                
                                # If attribute_value is string try to convert it
                                if(isinstance(attribute_value, str)):
                                    try:
                                        attribute_value = float(attribute_value)
                                    except ValueError:
                                        pass

                                output_dict[name] = attribute_value

                        else:
                            # If attribute_value is string try to convert it
                            if(isinstance(attribute, str)):
                                try:
                                    attribute = float(attribute)
                                except ValueError:
                                    pass
                            output_dict[output_attribute_name] = attribute
                    
                    for o in self.outputs:
                        # Send out the dictionary with the output component
                        o.send_out(output_dict=output_dict,
                                datetime_timestamp=self.iso8601ToDatetime(timestamps[sample]))

                # Set last timestamp to the last sample's timestamp
                self.last_timestamp = timestamps[-1]

                if(self.production_mode):
                    # Also change config file so if adapter crashes and reruns it
                    # continues from where it finished
                    with open(self.configuration_path) as data_file:
                        conf = json.load(data_file)
                        conf["from"] = self.last_timestamp
                
                    # Write the content back
                    with open(self.configuration_path, "w") as f:
                        json.dump(conf, f)

                # API is limited to 10000 samples per respons, so if that count is
                # reached one should probably repeat the call
                if(total_samples_obtained == 10000):
                    self.obtain()

    def obtain_periodically(self) -> None:
        # A method that periodicly calls the obtain method every
        # time_between_samples seconds
        while(True):
            self.obtain()
            sleep(self.time_between_samples)

    def iso8601ToUnix(self, iso8601Time: str) -> float:
        # Transforms iso8601 time format to unix time

        # TODO: if needed configure to right timezone
        parsed = iso8601.parse_date(iso8601Time)
        timetuple = parsed.timetuple()
        return time.mktime(timetuple)

    def iso8601ToDatetime(self, iso8601Time: str) -> Any:
        return iso8601.parse_date(iso8601Time)
