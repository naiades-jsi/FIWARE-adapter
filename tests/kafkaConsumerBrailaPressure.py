from json import loads
from kafka import KafkaConsumer, TopicPartition

consumer = KafkaConsumer(
     bootstrap_servers=['localhost:9092'],
     auto_offset_reset='latest',
     enable_auto_commit=False,
     group_id='my-group',
     value_deserializer=lambda x: loads(x.decode('utf-8')))

#assign topic to read from
tp = TopicPartition('measurements_node_braila_pressure5770', 0)
consumer.assign([tp])

for message in consumer:
    print(message.value["value"])
    print(type(message.value["value"]))