from fastapi import FastAPI

from kafka import KafkaConsumer

def obtener_datos_kafka():
    k = KafkaConsumer()