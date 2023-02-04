import kafka as k
import time
#from kafka_consumer import ConsumirKafka

def main():
    correr = True
    try:
        consumidor = k.KafkaConsumer("pendientes", bootstrap_servers="cc_kafka:9092", auto_offset_reset='earliest', enable_auto_commit=True, group_id='cc_consumer_gr')
        consumidor.subscribe("pendientes")
        while(correr):
            resultado = consumidor.poll(timeout_ms=5.0)
            print(resultado)
    except Exception as ex:
        print(ex)

main()

# def escuchar(srv="cc_kafka:9092", topic="pendientes", group_id="cc_consumer_gr"):
#     consumidor_kafka = ConsumirKafka(srv, topic, group_id)
#     consumidor_kafka.bucle_lector_mensajes()


# escuchar("cc_kafka:9092", "pendientes", "cc_consumer_gr")


# def bucle_lector_mensajes(topic, gr, srv):
# consumidor = k.KafkaConsumer('pendientes', group_id='cc_consumer_gr', bootstrap_servers=['cc_kafka:9092'], auto_offset_reset='earliest', enable_auto_commit=False)
# try:
#     correr = True
#     consumidor.subscribe('pendientes')
#     while(correr):
#         msj = consumidor.poll(timeout_ms=1)
#         if msj is None:
#             continue
#         else:
#             print("EL MENSAJE OBTENIDOO ES")
#             print(msj)
#             break
# except Exception as e:
#     raise e
# finally:
#     consumidor.close()

#bucle_lector_mensajes('pendientes', 'cc_consumer_gr', 'cc_kafka:9092')