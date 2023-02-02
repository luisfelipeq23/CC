from kafka import KafkaProducer
import json

class kafka_productor():
    __repo_name = ""
    __repo_url = ""
    __topic = ""

    def __init__(self, repo_name, repo_url, topic):
        self.__repo_name = repo_name
        self.__repo_url = repo_url
        self.__topic = topic
    
    def enviar_mensaje_kafka(self):
        productor = KafkaProducer(bootstrap_servers=['cc_kafka:9092'])
        #s, api_version=(0, 10, 0), value_serializer=lambda v: json.dumps(mensaje).encode('utf-8'))
        mensaje = self.__repo_name + "," + self.__repo_url
        print(mensaje)
        productor.send(self.__topic, mensaje.encode("UTF-8"))
