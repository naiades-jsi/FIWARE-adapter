from abc import ABC, abstractmethod
from typing import Any, Dict, List
from influxdb_client import InfluxDBClient
from influxdb_client.client.write_api import SYNCHRONOUS, ASYNCHRONOUS
import json
import csv
import os
import datetime

from kafka import KafkaProducer


class Output(ABC):
    from_hour: Any
    to_hour: Any
    field_names: List[str]

    @abstractmethod
    def configure(self, conf: Dict[Any, Any]) -> None:
        # Filed names
        self.field_names = conf["field_names"]

        # Filtering to hours in day
        if("from_hour" in conf and "to_hour" in conf):
            self.from_hour = eval(conf["from_hour"])
            self.to_hour = eval(conf["to_hour"])
        else:
            self.from_hour = None
            self.to_hour = None

    @abstractmethod
    def send_out(self, output_dict: Dict[str, Any],
                 datetime_timestamp: Any) -> None:
        pass

    def time_in_range(self, x: Any) -> bool:
        # Return true if x (in datetime.datetime fomat) is in the range [start, end]
        x = x.time()

        if self.from_hour <= self.to_hour:
            return self.from_hour <= x <= self.to_hour
        else:
            return self.from_hour <= x or x <= self.to_hour

class KafkaOutput(Output):
    # An output class that outputs a dictionary to a kafka topic

    producer: Any
    topic: str
    bootstrap_server: str

    def configure(self, conf: Dict[Any, Any]) -> None:
        self.topic = conf["topic"]
        self.bootstrap_server = conf["bootstrap_server"]

        # Initializes kafka producer with specified server
        self.producer = KafkaProducer(bootstrap_servers=
                                      [self.bootstrap_server],
                                      value_serializer=lambda x:
                                      json.dumps(x).encode('utf-8'))

        super().configure(conf=conf)

    def send_out(self, output_dict: Dict[str, Any],
                 datetime_timestamp: Any) -> None:
        # Execute the send out if time is in range (if that is required)
        if(self.from_hour is None or self.to_hour is None or self.time_in_range(datetime_timestamp)):
            # A method that sends (a dictionary) out a message to the topic
            self.producer.send(self.topic, value=output_dict)


class TerminalOutput(Output):
    # An output class that outputs a dictionary to the terminal

    def configure(self, conf: Dict[Any, Any]) -> None:
        super().configure(conf=conf)

    def send_out(self, output_dict: Dict[str, Any],
                 datetime_timestamp: Any) -> None:
        # Execute the send out if time is in range (if that is required)
        if(self.from_hour is None or self.to_hour is None or self.time_in_range(datetime_timestamp)):
            print(output_dict)


class FileOutput(Output):
    file_name: str
    file_path: str
    mode: str

    def __init__(self, conf: Dict[Any, Any] = None) -> None:
        super().__init__()
        if(conf is not None):
            self.configure(conf=conf)

    def configure(self, conf: Dict[Any, Any] = None) -> None:
        super().configure(conf=conf)
        self.file_name = conf["file_name"]
        self.mode = conf["mode"]
        self.file_path = "dump/" + self.file_name

        # make log folder if one does not exist
        dir = "./dump"
        if not os.path.isdir(dir):
            os.makedirs(dir)

        # If mode is write clear the file
        if(self.mode == "w"):
            if(self.file_name[-4:] == "json"):
                with open(self.file_path, "w") as f:
                    d = {
                        "data": []
                    }
                    json.dump(d, f)
            elif(self.file_name[-3:] == "csv"):
                with open(self.file_path, "w", newline="") as csvfile:
                    writer = csv.DictWriter(csvfile,
                                            fieldnames=self.field_names)
                    writer.writeheader()

    def send_out(self, output_dict: Dict[str, Any],
                 datetime_timestamp: Any) -> None:
        # Execute the send out if time is in range (if that is required)
        if(self.from_hour is None or self.to_hour is None or self.time_in_range(datetime_timestamp)):
            if(self.file_name[-4:] == "json"):
                self.write_JSON(output_dict=output_dict)
            elif(self.file_name[-3:] == "csv"):
                self.write_csv(output_dict=output_dict)
            else:
                print("Output file type not supported.")

    def write_JSON(self, output_dict: Dict[str, Any]) -> None:
        # Read content of file and add output_dict
        with open(self.file_path) as json_file:
            data = json.load(json_file)
            temp = data["data"]
            temp.append(output_dict)
        
        # Write the content back
        with open(self.file_path, "w") as f:
            json.dump(data, f)

    def write_csv(self, output_dict: Dict[str, Any]) -> None:
        with open(self.file_path, 'a', newline='') as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=self.field_names)
            writer.writerow(output_dict)


class InfluxOutput(Output):
    ip: str
    port: str
    token: str
    org: str
    bucket: str
    measurement: str
    tags: Dict
    output_timestamp_name: str

    influx_writer: Any

    def __init__(self, conf: Dict[Any, Any] = None) -> None:
        super().__init__()
        if(conf is not None):
            self.configure(conf=conf)

    def configure(self, conf: Dict[Any, Any] = None) -> None:
        super().configure(conf=conf)

        # Configura writer
        self.ip = conf["ip"]
        self.port = conf["port"]
        self.token = conf["token"]
        self.org = conf["org"]
        url = "http://" + self.ip + ":" + self.port

        self.influx_writer = InfluxDBClient(url=url, token=self.token,
                                            org=self.org).write_api(write_options=ASYNCHRONOUS)

        self.bucket = conf["bucket"]
        self.measurement = conf["measurement"]
        self.tags = eval(conf["tags"])
        self.output_timestamp_name = conf["output_timestamp_name"]


    def send_out(self, output_dict: Dict[str, Any],
                 datetime_timestamp: Any) -> None:
        # Remove timestamp from output dictionary
        # NOTE: timestamp MUST be in nanoseconds
        timestamp = int(output_dict[self.output_timestamp_name]*1000000000)
        only_values = output_dict
        del only_values[self.output_timestamp_name]

        # Write to database
        self.influx_writer.write(self.bucket, self.org,
                                 [{"measurement": self.measurement,
                                   "tags": self.tags, "fields": only_values,
                                   "time": timestamp}])
