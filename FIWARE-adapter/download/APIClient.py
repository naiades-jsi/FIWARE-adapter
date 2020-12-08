import json

from typing import Any, Dict, List, Optional
import requests

from download.output import Output, KafkaOutput


class NaiadesClient():
    ip: str
    port: str
    fiware_service: str
    entity_id: str
    required_attributes: List[str]
    output_attributes_names: List[str]
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
        self.required_attributes = conf["required_attributes"]
        if("output_attributes_names" in conf):
            self.output_attributes_names = conf["output_attributes_names"]
        else:
            self.output_attributes_names = self.required_attributes

        assert len(self.required_attributes) > 0, "Required attributes must be specified"

        # Base url construction
        self.base_url = "http://" + self.ip + ":" + self.ip +\
                        "/v2/entities/" + self.entity_id + "?attrs=" +\
                        self.required_attributes[0]
        for a in self.required_attributes[1:]:
            self.base_url = self.base_url + "," + a

        # Headers construction
        self.headers = {
            "Fiware-Service": self.fiware_service,
            "Fiware-service-path": "/",
            "Content-type": "application/json"
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
        if(self.last_timestamp is not None):
            url = self.base_url + "fromDate=" + self.last_timestamp
        else:
            url = self.base_url
        r = requests.get(url, headers=self.headers)
