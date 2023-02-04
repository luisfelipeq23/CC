import json
from fastapi import FastAPI
from cc_worker_github import worker_github

app = FastAPI()

ARCH_CREDENCIALES = './credenciales_minio.json'
RUTA_TMP_DESCARGA = "/repo_descargas/"

@app.post("/procesar_tarea")
async def procesar_tarea(data:str):
    mensaje = data
    print(data)
    repo_url = ""
    try:
        worker_gh = worker_github(repo_url, RUTA_TMP_DESCARGA)
        worker_gh.descargar_repo()
        repo_nombre = repo_url.split("/")[-1:]

        credenciales = obtener_credenciales()

        worker_minio = worker_minio(credenciales[0], credenciales[1], credenciales[2], repo_nombre[0], repo_nombre[0], RUTA_TMP_DESCARGA)
        worker_minio.subir_archivo()
        mensaje = 'status:200'
    except Exception as e:
        mensaje = 'status:400|' + e
    return {mensaje}

def obtener_credenciales():
    try:
        file = open(ARCH_CREDENCIALES, 'r')
        data = json.loads(file.read())
        file.close()
        return [data['url'], data['accessKey'], data['secretKey']]
    except Exception as e:
        return e
