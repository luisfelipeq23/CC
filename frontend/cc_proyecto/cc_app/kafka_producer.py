from kafka import KafkaProducer
import json

class kafka_productor():
    __repo_name = ""
    __repo_url = ""
    __topic = ""
    __servidor = ""

    def __init__(self, repo_name, repo_url, topic, servidor):
        self.__repo_name = repo_name
        self.__repo_url = repo_url
        self.__topic = topic
        self.__servidor = servidor
    
    def enviar_mensaje_kafka(self):
        productor = KafkaProducer(bootstrap_servers=[self.__servidor])
        #s, api_version=(0, 10, 0), value_serializer=lambda v: json.dumps(mensaje).encode('utf-8'))
        mensaje = self.__repo_name + "," + self.__repo_url
        mensaje = json.dumps(mensaje).encode('utf-8')
        print(mensaje)
        productor.send(self.__topic, mensaje)
