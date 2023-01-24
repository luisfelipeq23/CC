import json
from fastapi import FastAPI
from pydantic import BaseModel
from cc_worker_github import worker_github
from cc_worker_minio import worker_minio

app = FastAPI()

class RepoModel(BaseModel):
    repo_url: str
    ruta_descarga: str

ARCH_CREDENCIALES = './credenciales_minio.json'

@app.post("/init_worker/")
async def init_worker(repo:RepoModel):
    mensaje = ""
    try:
        worker_gh = worker_github(repo.repo_url, repo.ruta_descarga)
        worker_gh.descargar_repo()
        repo_nombre = repo.repo_url.split("/")[-1:]

        credenciales = obtener_credenciales()

        worker_minio = worker_minio(credenciales[0], credenciales[1], credenciales[2], repo_nombre[0], repo_nombre[0], repo.ruta_descarga)
        worker_minio.subir_archivo()
        mensaje = 'status:200'
    except Exception as e:
        mensaje = e
    return {mensaje}

def obtener_credenciales():
    file = open(ARCH_CREDENCIALES, 'r')
    data = json.loads(file.read())
    file.close()
    return [data['url'], data['accessKey'], data['secretKey']]
