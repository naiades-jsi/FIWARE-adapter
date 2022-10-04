A Client for NAIADES API that downloads data and puts them on Terminal, kafka topic or file.

# Requirements:
* iso8601: 0.1.14
* schedule: 1.0.0
* requests: 2.25.1
* kafka-python: 2.0.2

All requirements are also specified in requirements.txt file.

# Naiades Client:
The NaiadesClient gets data of a specified entity from the NAIADES historic API from a specified date by calling obtain() method. If obtain is called multiple times on the same object only new data will be obtained. Downloaded data is then send foward with output component.
The configuration file should contain the following fileds:
* production_mode: A boolean variable marking if conponent will be used in production. It then saves last timestamp downloaded so it can continue from there on in case of crash and rerun.
* ip: The IP address of the API. (eg. "5.53.108.182"),
* port: The port of the API (eg. "8668"),
* fiware_service: Fiware Service for the request (eg. "carouge"),
* entity_id: Id of the entity whose data we are obtaining. (eg. "urn:ngsi-ld:FlowerBed:FlowerBed-1"),
* required_attributes: Attributes that are to be obtained from the API. (eg. ["soilMoisture", "depth"]),
* output_attributes_names: Optional parameter containing a list of names of the attributes for the outputted object, corresponding with the required attributes. If an element of a list is a list of names then the cooresponding attribute must also be a list of the same length (eg. attribute nemed value in API contains [1, 24, 9] and we want to name elements "leak_state", "noise_dB", "spre_dB" (for example see client5981.json configuretion file)). If it is not specified the required_attributes are used as output names,
* output_timestampe_name: Optional parameter that defines the name under which the timestamp will be outputted. If it is not specified "timestamp" will be used. (eg. "time"),
* output_timestamp_format": Optional parameter that defines the format in which the outputted timestamp will be. If it is not specified "iso8601" will be used. (eg. "unix_time"),
* from: An optional parameter containing the date from which data will be obtained. If it is not specified all data is obtained. It should be in a SO8601 format (eg"2020-12-01T10:32:19.000"),
* outputs: A list of outputs. (eg. "KafkaOutput()"),
* output_configurations: A list of objects containing the configuration for the outputs.
If NaiadesClient is ran with DownloadScheduler one of the following fields must also be provided:
* seconds_between_samples: An integer representing the number of seconds between obtain calls,
* second_in_minute: A string that specifies at which second of a minute the obtain will be periodically called. (example: ":00"),
* minute_in_hour: A string that specifies at which minute of a hour the obtain function will be periodecally called (example: ":30"),
* hour_in_day: A string that specifies at which hour of day the obtain function will be periodecally called (example: "04:00").
If second_in_minute, minute_in_hour or hour_in_day is used an additional field can be specified:
* period: An integer that limits execusion of obtain function so it is not executed every minute (or hour or day) but every period-th time.

An example of configuration file can be seen in ..\config\brailaNoise2182.json

# Output:
A component that sends foward downloaded data. The following configuration fields are general for all outputs: 
* from_hour: A hour of day in datetime format used to filter samples in combination with to_hour (only sends out samples with timestamps during these hours). (eg. datetime.time(23, 0, 0) -> after 11pm)
* to_hour: A hour of day in datetime format used to filter samples in combination with from_hour (only sends out samples with timestamps during these hours). (eg. datetime.time(2, 0, 0) -> before 2am)

1. **Terminal output:** Prints data in terminal.

2. **Kafka output:** Sends data to kafka topic. The configuration file contains the following fields:
* topic: The kafka topic to which to publish messages. (eg. "APIClientTest"),
* bootstrap_server: The address of the kafka server. (eg. "localhost:9092")

3. **File output:** Writes data to a json (time consuming) or csv file which is saved to dump folder. The configuration file contains the following fields:
* file_name: A name of the output file. (example: "braila5770.csv"),
* mode": "w" for write or "a" for append

# Download Scheduler:
Combines multiple clients (multiple entities) and executes obtain calls as specified for each client. The configuration file contains the following field:
* clients: A list of configuration file names for individial clients 

# Pinging watchdog:
If -w flag is used when the component is run a ping is sent to watchdog every 30 seconds.

# Atena deployment:
The adapter is deployed on Atena server using a client/server system supervisor.

## FIWARE-adapter configuration files:
The FIWARE-adapter is ran with configurations specified in config/productionKafka directory. There is a seperate configuration file for every downloaded entity. File downloadScheduler.json is a configuration file for scheduler and contains a list of all entitie's configuration files that are to be downloaded. 

## Supervisor configuration file:
The configuration file for supervisor is located in /etc/supervisor/conf.d/naiades-fiware-adapter.conf. Bellow is the content of the configuration file:
```
[program:naiades_fiware_adapter]
command=/home/galp/enviroments/fiwareadapter/bin/python /mnt/data/services/naiades-fiware-adapter/FIWARE-adapter/main.py -c productionKafka/downloadScheduler.json -w
directory=/mnt/data/services/naiades-fiware-adapter/FIWARE-adapter
autostart=true
autorestart=true
stderr_logfile=/mnt/data/services/naiades-fiware-adapter/log/naiades-fiware-adapter.err.log
stdout_logfile=/mnt/data/services/naiades-fiware-adapter/log/naiades-fiware-adapter.out.log
```
/home/galp/enviroments/fiwareadapter contains an enviroment with all installed requirements. <br>
The actual Fiware adapter code is located in /mnt/data/services/naiades-fiware-adapter/FIWARE-adapter. <br>
The directory must be set to /mnt/data/services/naiades-fiware-adapter/FIWARE-adapter so all imports work as they should and the dump directory is created in the correct location.

## Supervisor commands:
After changing supervisor configuration run:
```sudo supervisorctl reread``` and <br>
```sudo supervisorctl update```. <br>

To start the service run:
```sudo supervisorctl start naiades_fiware_adapter```. <br>

To stop the service run:
```sudo supervisorctl stop naiades_fiware_adapter```. <br>

To check the status of the service run:
```sudo supervisorctl status naiades_fiware_adapter```.<br>
<br>

If the service crashes it will automatically rerun and continue download from there.

TODO:
* iso8601 to unix time conversion is done withou specifiing timezone. If needed that is to be fixed.
* Do the same with subscription.