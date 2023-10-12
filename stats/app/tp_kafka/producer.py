from aiokafka import AIOKafkaProducer
from app.settings import KAFKA_URI


producer = AIOKafkaProducer(bootstrap_servers=KAFKA_URI)