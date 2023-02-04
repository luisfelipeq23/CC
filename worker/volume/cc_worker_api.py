import json
from fastapi import FastAPI, Body
from cc_worker_github import worker_github
from pydantic import BaseModel
import os

app = FastAPI()

ARCH_CREDENCIALES = './credenciales_minio.json'
RUTA_TMP_DESCARGA = "/repo_descargas/"

def crear_folder(name):
    home_dir = os.path.expanduser("~")
    new_dir = os.path.join(home_dir, name)
    if not os.path.exists(new_dir):
        os.makedirs(new_dir)

class Tareas(BaseModel):
    url:str

@app.post("/procesar_tarea/")
async def procesar_tarea(tareas: Tareas):
    repo_url = tareas.url
    print(repo_url)
    crear_folder(RUTA_TMP_DESCARGA)
    try:
        worker_gh = worker_github(repo_url, RUTA_TMP_DESCARGA)
        worker_gh.descargar_repo()
        repo_nombre = repo_url.split("/")[-1:]

        credenciales = obtener_credenciales()

        print("credenciales:" + credenciales)

        worker_minio = worker_minio(credenciales[0], credenciales[1], credenciales[2], repo_nombre[0], repo_nombre[0], RUTA_TMP_DESCARGA)
        worker_minio.subir_archivo()
        mensaje = 'status:200'
    except Exception as e:
        mensaje = 'status:400'
    return {mensaje}

def obtener_credenciales():
    try:
        file = open(ARCH_CREDENCIALES, 'r')
        data = json.loads(file.read())
        file.close()
        return [data['url'], data['accessKey'], data['secretKey']]
    except Exception as e:
        return e
