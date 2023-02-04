import kafka as k
import requests
import tracemalloc
from fastapi import FastAPI

tracemalloc.start()

url = "http://cc_worker:3000/procesar_tarea/"

# app = FastAPI()

# @app.post("/enviar_peticion")
# async 
def enviar_peticion_worker(datos):
    try:
        payload = "{payload:" + str(datos) + "}"
        resp = requests.post(url,json=payload)
        if resp.status_code != 200:
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
                enviar_peticion_worker(msj)
    except Exception as ex:
        print(ex)

main()



# response = requests.get(url)

# if response.status_code == 200:
#     data = response.json()
#     print(data)
# else:
#     print("Request failed with status code:", response.status_code)

# while(correr):
#     resultado = consumidor.poll(timeout_ms=5.0)
#     if(resultado != ""):
#         print(resultado)
#         time.sleep(1800)
