from kafka import KafkaConsumer
from api import logger
from dotenv import load_dotenv
import os

load_dotenv()

# poetry add kafka-python
def consumer_kafka():
    # brokers = ['localhost:29092', 'localhost:39092']
    # topics = 'test-topic'
    
    brokers = str(os.getenv("KAFKA_HOST", 'localhost:29092,localhost:39092')).split(",")
    topics = str(os.getenv("KAFKA_TOPIC", 'test-topic')).split(",")

    for topic in topics:
        consumer = KafkaConsumer(topic, group_id="Python_Kafka_Consumer_Job", bootstrap_servers=brokers)

        if consumer:
            for message in consumer:
                logger.info("{}, {}, {}".format(message, message.value, message.value.decode("utf-8")))