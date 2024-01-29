from kafka import KafkaConsumer
from api import logger
from dotenv import load_dotenv
import os
import json
from threading import Thread

load_dotenv()

# poetry add kafka-python
def consumer_kafka(doc, topic):
    # brokers = ['localhost:29092', 'localhost:39092']
    # topics = 'test-topic'
    brokers = str(os.getenv("KAFKA_HOST", doc['app']['kafka']['host'])).split(",")
    
    consumer = KafkaConsumer(topic, group_id="Python_Kafka_Consumer_Job", bootstrap_servers=brokers)
    for message in consumer:
        logger.info("{}, {}, {}".format(message, message.value, message.value.decode("utf-8")))
