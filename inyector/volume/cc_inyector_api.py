import kafka as k
import requests
import tracemalloc
import json

tracemalloc.start()
#https://github.com/acheong08/ChatGPT.git
def enviar_peticion_worker(datos):
    url = "http://cc_worker:3000/procesar_tarea/"
    try:
        url = datos
        print(url)
        resp = requests.post(url,json=url)
        if resp.status_code != 200:
            print(resp.json())
            print("Solicitud no enviada")
        else:
            print("Solicitud enviada con éxito")
    except Exception as e:
        print(e)

def main():
    try:
        consumidor = k.KafkaConsumer("pendientes", bootstrap_servers="cc_kafka:9092")
        consumidor.subscribe("pendientes")
        for msj in consumidor:
            if msj:
                datos = msj.value
                datos = datos.decode('utf-8')
                print(datos)
                enviar_peticion_worker(datos)
    except Exception as ex:
        print(ex)

main()
