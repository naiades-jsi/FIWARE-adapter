from abc import ABC, abstractmethod
from typing import Any, Dict, List
import json
import csv
import os

from kafka import KafkaProducer


class Output(ABC):
    @abstractmethod
    def configure(self, conf: Dict[Any, Any]) -> None:
        pass

    @abstractmethod
    def send_out(self, output_dict: Dict[str, Any]) -> None:
        pass


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

    def send_out(self, output_dict: Dict[str, Any]) -> None:
        # A method that sends (a dictionary) out a message to the topic
        self.producer.send(self.topic, value=output_dict)


class TerminalOutput(Output):
    # An output class that outputs a dictionary to the terminal

    def configure(self, conf: Dict[Any, Any]) -> None:
        pass

    def send_out(self, output_dict: Dict[str, Any]) -> None:
        print(output_dict)


class FileOutput(Output):
    file_name: str
    file_path: str
    mode: str
    field_names: List[str]

    def __init__(self, conf: Dict[Any, Any] = None) -> None:
        super().__init__()
        if(conf is not None):
            self.configure(conf=conf)

    def configure(self, conf: Dict[Any, Any] = None) -> None:
        self.file_name = conf["file_name"]
        self.mode = conf["mode"]
        self.field_names = conf["field_names"]
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

    def send_out(self, output_dict: Dict[str, Any]) -> None:
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