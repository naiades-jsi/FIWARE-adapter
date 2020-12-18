from time import sleep
import json
import time
import iso8601

from typing import Any, Dict, List, Optional
import requests

from output import Output, KafkaOutput, TerminalOutput


class NaiadesClient():
    ip: str
    port: str
    fiware_service: str
    entity_id: str
    required_attributes: List[str]
    output_attributes_names: List[str]
    output_timestampe_name: str
    output_timestamp_format: str
    time_between_samples: float
    base_url: str
    headers: Dict[str, str]
    last_timestamp: str

    output: "Output"
    output_configuration: Dict[Any, Any]

    def __init__(self, configurationPath: str = None) -> None:
        self.configuration(configurationPath=configurationPath)

    def configuration(self, configurationPath: str = None) -> None:
        # Read config file
        with open(configurationPath) as data_file:
            conf = json.load(data_file)

        self.ip = conf["ip"]
        self.port = conf["port"]
        self.fiware_service = conf["fiware_service"]
        self.entity_id = conf["entity_id"]
        self.time_between_samples = conf["time_between_samples"]
        self.required_attributes = conf["required_attributes"]
        # If config file contains output_timestampe_name set it from there,
        # otherwise set it to timestamp
        if("output_timestampe_name" in conf):
            self.output_timestampe_name = conf["output_timestampe_name"]
        else:
            self.output_timestampe_name = "timestamp"
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

        # Configure output
        self.output = eval(conf["output"])
        self.output_configuration = conf["output_configuration"]
        self.output.configure(self.output_configuration)

    def obtain(self) -> None:
        # A method that obtains data (since last timestamp if specified)
        # from API

        # If last timestamp is not None add it to the url parameters
        if(self.last_timestamp is not None):
            url = self.base_url + "&fromDate=" + self.last_timestamp
        else:
            url = self.base_url

        # Send the get request
        r = requests.get(url, headers=self.headers)

        # If status code is not 200 raise an error
        if(r.status_code != requests.codes.ok):
            r.raise_for_status()

        # Retrieve attributest and timestamps from body of response
        body = r.json()
        attributes = body["attributes"]
        timestamps = body["index"]

        number_of_samples = len(timestamps)

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
                output_dict = {self.output_timestampe_name: t}
                for i in range(len(self.required_attributes)):
                    output_attribute_name = self.output_attributes_names[i]
                    attribute = attributers_dict[self.required_attributes[i]][sample]
                    # If output_attribute_name is a list that means that 
                    # attribute is also a list and elements of the list are
                    # added to the output_dict.
                    if(isinstance(output_attribute_name, list)):
                        if(not isinstance(attribute, list)):
                            print("Incompatible output names specification.")
                            exit(1)
                        for name_idx in range(len(output_attribute_name)):
                            name = output_attribute_name[name_idx]
                            output_dict[name] = attribute[name_idx]

                    else:
                        output_dict[output_attribute_name] = attribute
                # Send out the dictionary with the output component
                self.output.send_out(output_dict=output_dict)

            # Set last timestamp to the last sample's timestamp
            self.last_timestamp = timestamps[-1]

    def obtain_periodically(self) -> None:
        # A method that periodicly calls the obtain method every
        # time_between_samples seconds
        while(True):
            self.obtain()
            sleep(self.time_between_samples)

    def iso8601ToUnix(self, iso8601Time: str) -> float:
        # Transforms iso8601 time format to unix time

        # TODO: if needed configure to right timezon
        parsed = iso8601.parse_date(iso8601Time)
        timetuple = parsed.timetuple()
        return time.mktime(timetuple)
