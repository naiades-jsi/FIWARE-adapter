The NaiadesClient gets data from the NAIADES historic API from a specified date by calling obtain() method. If obtain is called multiple times on the same object only new data will be obtained. 
The data obtained is then passed on to a kafka server.
The configuration of the client is defined in the configuration file that should be specified when initializing a NaiadesClient object (by specifiing path to the file eg. .\config\APIClientConfiguration.json). 

# Configuration file
The configuration file should contain the following fileds:
* ip: The IP address of the API. (eg. "5.53.108.182"),
* port: The port of the API (eg. "8668"),
* fiware_service: Fiware Service for the request (eg. "carouge"),
* entity_id: Id of the entity whose data we are obtaining. (eg. "urn:ngsi-ld:FlowerBed:FlowerBed-1"),
* required_attributes: Attributes that are to be obtained from the API. (eg. ["soilMoisture", "depth"]),
* output_attributes_names: Names of the attributes for the outputted object, corresponding with the required attributes. Timestamp is always added as timestamp. (eg.["soil_moisture", "depth"]),
* from: An optional parameter containing the date from which data will be obtained. If it is not specified all data is obtained. It should be in a SO8601 format (eg"2020-12-01T10:32:19.000"),
* output: The output type (eg. "KafkaOutput()"),
* output_configuration: An object containing the configuration for the output containing the following fields (for KafkaOutput):
   * topic: The kafka topic to which to publish messages. (eg. "APIClientTest"),
   * bootstrap_server: The address of the kafka server. (eg. "localhost:9092")

An example of configuration file can be seen in ..\config\APIClientConfiguration.json

# Example:
APIClientTest file contains an example of running the clinet and kafkaConsumer file contains the corresponding kafka consumer that reades messages from topic and prints them.

In APIClientTest the obtain method is called every time_interval seconds where time interval contains the expected time between two samples in API.

TODO:
Do the same with subscription.