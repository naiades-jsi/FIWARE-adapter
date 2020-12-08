from abc import ABC, abstractmethod
from typing import Any, Dict

class Output(ABC):
    @abstractmethod
    def configure(self, conf: Dict[Any, Any]) -> None:
        pass
    
    @abstractmethod
    def sendOut(sefl) -> None:
        pass

class KafkaOutput(Output):

    def configure(self, conf: Dict[Any, Any]) -> None:
        pass

    def sendOut(sefl) -> None:
        pass