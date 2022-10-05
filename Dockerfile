# BUILDING: docker build -t e3ailab/fiware_adapter_ircai .
# PUSHING: docker push e3ailab/fiware_adapter_ircai
# RUNNING: docker run -d --network=host e3ailab/fiware_adapter_ircai

FROM ubuntu:20.04
RUN apt-get update -y && \
    apt-get install -y python3-pip python3-dev
COPY ./requirements.txt /requirements.txt
WORKDIR /
RUN pip3 install -r requirements.txt
COPY . /

# e3ailab/fiware_adapter_ircai
CMD ["python3", "main.py", "-c", "productionSIMAVI/downloadScheduler.json"]