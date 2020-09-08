# NAIADES Toolkit (for streaming)
Tools for NAIADES stream processing engine include external tools, that will be updated for the use in NAIADES. External tools are linked as Git submodules.

It includes the following solutions:

| Name | Description |
| :--- | :--- |
| iot-rapids | Framework for storing IoT and external streaming data sources. The framework includes a crawlers' system for downloading external data sources such as publicly available ground- and surface water datasets, weather data and similar. |
| iot-fusion | Framework for heterogeneous streaming data fusion. It can generate uniform and coherent feature vectors in an on-line scenario from a set of streaming sources (e. g. IoT data stream, weather forecasts, current weather data and additional use-case related antropogenic data). The vectors can be then sent to an external modeling component or an internal modeling/anomaly detection service can be used. |
| ml-rapids | Very fast library with the implementation of incremental learning methods. Currently the methods are exported to Python; integration into NodeJS is planned. |
| forecasting | Python (currently `2.7.x`; should be upgraded) module that can ingest data from `iot-fuson` and generate predictions based on a pre-trained model. Model training is closely coupled with `iot-fusion` functionalities. |
| streamstory-py | A Python clone of a [StreamStory project](https://github.com/JozefStefanInstitute/StreamStory). It will be developed in collaboration with the FACTLOG project. Alternatively, we can upgrade the existing repository. |

Most of the components are loosely coupled via a Kafka interface.
