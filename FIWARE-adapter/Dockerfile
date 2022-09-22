# BUILDING: docker build -t <container_name> .
# RUNNING: docker run <container_name>
# e.g. docker run fiware_adapter
FROM ubuntu:20.04
RUN apt-get update -y && \
    apt-get install -y python3-pip python3-dev
COPY ./requirements.txt /requirements.txt
WORKDIR /
RUN pip3 install -r requirements.txt
COPY . /
<<<<<<< HEAD

# e3ailab/fiware_adapter_ircai
=======
>>>>>>> aae87cb1c70c29e90f82ce7a48cb7d1aec3a2eb7
CMD ["python3", "main.py", "-c", "productionSIMAVI/downloadScheduler.json"]