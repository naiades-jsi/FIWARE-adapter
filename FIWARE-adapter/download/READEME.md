The NaiadesClient gets data of a specified entity from the NAIADES historic API from a specified date by calling obtain() method. If obtain is called multiple times on the same object only new data will be obtained. 
The data obtained is then passed on to a kafka server in a specified form.
The configuration of the client is defined in the configuration file that should be specified when initializing a NaiadesClient object (by specifiing path to the file eg. .\config\APIClientConfiguration.json). 

# Requirements:
* iso8601: 0.1.14
* schedule: 1.0.0
* requests: 2.25.1
* kafka-python: 2.0.2

# Configuration file
The configuration file should contain the following fileds:
* ip: The IP address of the API. (eg. "5.53.108.182"),
* port: The port of the API (eg. "8668"),
* fiware_service: Fiware Service for the request (eg. "carouge"),
* entity_id: Id of the entity whose data we are obtaining. (eg. "urn:ngsi-ld:FlowerBed:FlowerBed-1"),
* time_between_samples: Approximate time in seconds between two samples. (eg. 60)
* required_attributes: Attributes that are to be obtained from the API. (eg. ["soilMoisture", "depth"]),
* output_attributes_names: Optional parameter containing a list of names of the attributes for the outputted object, corresponding with the required attributes. If an element of a list is a list of names then the cooresponding attribute must also be a list of the same length (eg. attribute nemed value in API contains [1, 24, 9] and we want to name elements "leak_state", "noise_dB", "spre_dB" (for example see client5981.json configuretion file)). If it is not specified the required_attributes are used as output names,
* output_timestampe_name: Optional parameter that defines the name under which the timestamp will be outputted. If it is not specified "timestamp" will be used. (eg. "time"),
* output_timestamp_format": Optional parameter that defines the format in which the outputted timestamp will be. If it is not specified "iso8601" will be used. (eg. "unix_time"),
* from: An optional parameter containing the date from which data will be obtained. If it is not specified all data is obtained. It should be in a SO8601 format (eg"2020-12-01T10:32:19.000"),
* output: The output type (eg. "KafkaOutput()"),
* output_configuration: An object containing the configuration for the output containing the following fields (for KafkaOutput):
   * topic: The kafka topic to which to publish messages. (eg. "APIClientTest"),
   * bootstrap_server: The address of the kafka server. (eg. "localhost:9092")

An example of configuration file can be seen in ..\config\APIClientConfiguration.json

# Example:
APIClientTest file contains an example of running the clinet in a loop and APIClientTest2 file contains an example of running obtain method manualy.

TODO:
* iso8601 to unix time conversion is done withou specifiing timezone. If needed that is to be fixed.
* Do the same with subscription.