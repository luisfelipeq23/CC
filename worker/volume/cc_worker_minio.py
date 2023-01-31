import os
import re
from minio import Minio


class worker_minio:

    __servidor = ""
    __clave_acceso = ""
    __clave_secreta = ""
    __nombre_bucket = ""
    __repo_nombre = ""
    __ruta_local_fichero = ""

    def __init__(self, servidor, clave_acceso, clave_secreta, nombre_bucket, repo_nombre, ruta_local_fichero):
        self.__servidor = servidor
        self.__clave_acceso = clave_acceso.strip()
        self.__clave_secreta = clave_secreta.strip()
        self.__nombre_bucket = self.limpiar_nombre_bucket(nombre_bucket.strip())
        self.__repo_nombre = repo_nombre.strip()
        self.__ruta_local_fichero = ruta_local_fichero.strip()
    
    def limpiar_nombre_bucket(self, nombre_bucket):
        try:
            nombre_bucket = re.sub(r'\W+', '-', nombre_bucket)
            nombre_bucket = nombre_bucket.lower()
            return nombre_bucket
        except Exception as e:
            print(e)
    
    def subir_archivo(self):
        try:
            # Obtener cliente
            cliente = Minio(endpoint=self.__servidor, access_key=self.__clave_acceso, secret_key=self.__clave_secreta, secure=False)

            # Crear 'cc.bucket' bucket si no existe.
            found = cliente.bucket_exists(self.__nombre_bucket)
            if not found:
                cliente.make_bucket(self.__nombre_bucket)

            # Subir el archivo al bucket correspondiente
            for raiz, dirs, archivos in os.walk(self.__ruta_local_fichero):
                for archivo in archivos:
                    cliente.fput_object(self.__nombre_bucket, os.path.join(raiz, archivo).replace(self.__ruta_local_fichero, ""), os.path.join(raiz, archivo))
            
        except Exception as e:
            print(e)
