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
    producer: Any
    topic: str
    bootstrap_server: str

    def configure(self, conf: Dict[Any, Any]) -> None:
        self.topic = conf["topic"]
        self.bootstrap_server = conf["bootstrap_server"]

        self.producer = KafkaProducer(bootstrap_servers=\
                                      [self.bootstrap_server],
                                      value_serializer=lambda x: 
                                      dumps(x).encode('utf-8'))

    def send_out(self, output_dict: Dict[str, Any]) -> None:
        self.producer.send(self.topic, value=output_dict)


class TerminalOutput(Output):
    def configure(self, conf: Dict[Any, Any]) -> None:
        pass

    def send_out(self, output_dict: Dict[str, Any]) -> None:
        print(output_dict)