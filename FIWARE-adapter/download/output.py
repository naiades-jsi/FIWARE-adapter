from abc import ABC, abstractmethod
from typing import Any, Dict
from json import dumps

from kafka import KafkaProducer


class Output(ABC):
    @abstractmethod
    def configure(self, conf: Dict[Any, Any]) -> None:
        pass

    @abstractmethod
    def send_out(self, output_dict: Dict[str, Any]) -> None:
        pass


class KafkaOutput(Output):
    # An output class that outputs a dictioneary to a kafka topic

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
                                      dumps(x).encode('utf-8'))

    def send_out(self, output_dict: Dict[str, Any]) -> None:
        # A method that sends (a dictionary) out a message to the topic
        self.producer.send(self.topic, value=output_dict)


class TerminalOutput(Output):
    # An output class that outputs a dictionary to the terminal

    def configure(self, conf: Dict[Any, Any]) -> None:
        pass

    def send_out(self, output_dict: Dict[str, Any]) -> None:
        print(output_dict)
