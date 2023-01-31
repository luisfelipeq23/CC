from kafka import KafkaConsumer

class inyector:

    __topic = ""

    def __init__(self, topic):
        self.__topic = topic

    def obtener_mensaje_kafka(self):
        try:
            consumidor = KafkaConsumer(self.__topic, bootstrap_servers='cc_kafka:9092')
            consumidor.subscribe(self.__topic)
            mensajes = consumidor.poll()
            for msg in mensajes:
                return str(msg)
        except Exception as e:
            print(e)

    def obtener_topic(self):
        return self.__topic
    
    def escribir_topic(self, topic):
        self.__topic = topic

# 192.168.0.6
i = inyector('pendientes')
i.obtener_mensaje_kafka()