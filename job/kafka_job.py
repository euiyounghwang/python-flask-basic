from kafka import KafkaConsumer
from api import logger
from dotenv import load_dotenv
import os
import json

load_dotenv()

# poetry add kafka-python
def consumer_kafka(doc):
    # brokers = ['localhost:29092', 'localhost:39092']
    # topics = 'test-topic'
    brokers = str(os.getenv("KAFKA_HOST", doc['app']['kafka']['host'])).split(",")
    topics =  os.getenv("KAFKA_TOPIC", doc['app']['kafka']['topic']).split(",")

    for topic in topics:
        consumer = KafkaConsumer(topic, group_id="Python_Kafka_Consumer_Job", bootstrap_servers=brokers)

        if consumer:
            for message in consumer:
                logger.info("{}, {}, {}".format(message, message.value, message.value.decode("utf-8")))