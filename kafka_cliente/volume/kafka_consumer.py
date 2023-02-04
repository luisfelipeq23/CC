import kafka as k

def main():
    correr = True
    try:
        consumidor = k.KafkaConsumer("pendientes", bootstrap_servers="cc_kafka:9092")
        consumidor.subscribe("pendientes")
        while(correr):
            resultado = consumidor.poll(timeout_ms=5.0)
            print(resultado.decode("UTF-8"))
    except Exception as ex:
        print(ex)

main()

# class ConsumirKafka:

#     __bootstrap_servers = ""
#     __topic = ""
#     __group_id = ""
#     __consumer = None

#     def __init__(self, bootstrap_srv, topic, group_id):
#         self.__bootstrap_servers = bootstrap_srv
#         self.__topic = topic
#         self.__group_id = group_id
#         self.__consumer = k.KafkaConsumer(self.__topic, group_id=self.__group_id, bootstrap_servers=[self.__bootstrap_servers], auto_offset_reset='latest', enable_auto_commit=False)
    
#     def consumir_mensajes(self):
#         for message in self.__consumer:
#             print(message.topic + "," + message.partition + "," + message.offset + "," + message.key + "," + message.value)

#     def bucle_lector_mensajes(self):
#         try:
#             correr = True
#             self.__consumer.subscribe(topics=[self.__topic])
#             while(correr):
#                 msj = self.__consumer.poll(timeout_ms=1)
#                 if msj is None:
#                     continue
#                 else:
#                     print("EL MENSAJE OBTENIDOO ES")
#                     print(msj)
#                     break
#         except Exception as e:
#             raise e
#         finally:
#             self.__consumer.close()


# def bucle_lector_mensajes(consumidor, topic, gr, srv):
#     try:
#         correr = True
#         consumidor.subscribe(topics=topic)
#         while(correr):
#             msj = consumidor.poll(timeout_ms=1)
#             if msj is None:
#                 continue
#             else:
#                 print("EL MENSAJE OBTENIDOO ES")
#                 print(msj)
#                 break
#     except Exception as e:
#         raise e
#     finally:
#         consumidor.close()

# consumidor = k.KafkaConsumer('pendientes', group_id='cc_consumer_gr', bootstrap_servers=['cc_kafka:9092'], auto_offset_reset='latest', enable_auto_commit=False)
# bucle_lector_mensajes(consumidor, 'pendientes', 'cc_consumer_gr', 'cc_kafka:9092')











# from kafka import KafkaConsumer
# from fastapi import FastAPI
# from fastapi import FastAPI, BackgroundTasks

# app = FastAPI()

# @app.get("/escuchar/{kafka_url}/{topic}")
# async def escuchar_kafka(kafka_url: str, topic: str):
#     try:
#         background_task = BackgroundTasks()
#         consumidor = KafkaConsumer(topic, bootstrap_servers=kafka_url)
#         background_task.add_task(consumir_mensajes, consumidor)
#         return {"message": "Escuchando mensajes del Topic {} en {}".format(topic.decode('utf-8'), kafka_url)}
#     except Exception as e:
#         return e

# def consumir_mensajes(consumidor):
#     for msj in consumidor:
#         print(msj.value)

# escuchar_kafka('cc_kafka:9092','pendientes')