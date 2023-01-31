import json
from fastapi import FastAPI
from fastapi import FastAPI, BackgroundTasks
from kafka import KafkaConsumer

app = FastAPI()

@app.get("/escuchar/{kafka_url}/{topic}")
async def escuchar_kafka(kafka_url: str, topic: str):
    background_task = BackgroundTasks()
    consumidor = KafkaConsumer(topic, bootstrap_servers=kafka_url)
    background_task.add_task(consumir_mensajes, consumidor)
    return {"message": "Escuchando mensajes del Topic {} en {}".format(topic.decode('utf-8'), kafka_url)}

def consumir_mensajes(consumidor):
    for msj in consumidor:
        print(msj.value.decode())

while(True):
    escuchar_kafka('cc_kafka:9092','pendientes')