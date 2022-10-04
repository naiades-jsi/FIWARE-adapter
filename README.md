# NAIADES FIWARE adapter
This component is designed to periodically download samples from the NAIADES HISTORIC API and output it to either a file, kafka topic, influxdb or to the terminal. It is designed from two components: one for downloading and one (or more) for outputting the samples.

## Running
To run the code you only need to execute the main.py script with the following command:

```python main.py -c configuration file```

All the code is located in the download directory.

## Configuration
The configuration specified in the `-c` tag is the path to a configuration relative to the config directory. This is the main configuration file that only holds the field clients. This field contains a list of relative paths to the configuration files specific to each entity.

The subdirectory `config/productionKafka` contains all the configurations required for running the adapter for all required entities and outputting them to influx, kafka and file. The main configuration file in this case is `config/productionKafka/configurationScheduler.json`.

The subdirectory config/productionFile contains most of the configurations required for running the adapter and output the results to the files. The main configuration file in this case is `config/productionFile/configurationScheduler.json`.

The subdirectory `config/productionStreamStory` contains all of the configurations required for the stream story for running the adapter and output the results to the files. The main configuration file in this case is `config/productionStreamStory/configurationScheduler.json`.
