#!/usr/bin/env python
# pip3 install kafka-python
from kafka import KafkaConsumer, KafkaClient
from kafka import TopicPartition

bootstrap_servers='localhost:9092'
topic_name = "TOPIC_NAME"
group_id = "issue_finder" #Can call it whatever, do not set it to your existing group_id
consumer = KafkaConsumer(bootstrap_servers=bootstrap_servers,enable_auto_commit=False,group_id=group_id)


for p in consumer.partitions_for_topic(topic_name):
    tp = TopicPartition(topic_name, p)
    consumer.assign([tp])
    consumer.seek_to_beginning(tp)

try:
    for msg in consumer:
        print(msg)
except (KeyboardInterrupt, SystemExit):
    print("Consumption is interrupted!")
    consumer.close(autocommit=False)


#You can find the offset from the print'd messages
