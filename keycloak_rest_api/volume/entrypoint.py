import requests
import json
import socket
import docker

ACCESS_TOKEN_URL = "http://<ip>:8080/realms/<realm>/protocol/openid-connect/token"
ADD_USER_URL = "http://<ip>:8080/admin/realms/<realm>/users"
ADD_CLIENT_URL = "http://<ip>:8080/admin/realms/<realm>/clients"
ADD_REALM_URL = "http://<ip>:8080/admin/realms/"
CLIENT_SECRET_URL = "http://<ip>:8080/admin/clients/<realm>/clients/<id>/client-secret"

LISTA_URLs = [ACCESS_TOKEN_URL, ADD_USER_URL, ADD_CLIENT_URL, ADD_REALM_URL, CLIENT_SECRET_URL]

hostname = socket.gethostname()
ip_add = socket.gethostbyname(hostname)

import docker
import json

def get_container_data():
    DATA_DICT = {}
    client = docker.from_env()
    container_pattern = 'cc_*'
    containers = client.containers.list(all=True, filters={'name': container_pattern})
    for container in containers:
        container_name = container.attrs['Name']
        container_ip_address = container.attrs["NetworkSettings"]["Networks"]["cc_backend"]["IPAddress"]
        print(container_name + " " + "cc_backend" + " " + container_ip_address)

def get_container_data(container_name):
    DATA_DICT = {}
    client = docker.from_env()
    container = client.containers.get(container_name)
    ip_addr = container.attrs["NetworkSettings"]["Networks"]["cc_backend"]["IPAddress"]
    print(container_name + " " + "cc_backend" + " " + ip_addr)
    for i in range(len(LISTA_URLs)):
        LISTA_URLs[i] = LISTA_URLs[i].replace("<ip>",ip_addr)
        print(LISTA_URLs[i])

get_container_data('cc_keycloak')

for i in range(len(LISTA_URLs)):
    LISTA_URLs[i] = LISTA_URLs[i].replace("<ip>", "cc_keycloak")

def login_get_token_keycloak(in_user, in_password, in_realm, in_client, in_grant_type):
    try:
        payload = {
            'client_id': in_client,
            'username': in_user,
            'password': in_password,
            'grant_type': in_grant_type
        }
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded'
        }
        response = requests.post(url=LISTA_URLs[0].replace("<realm>", in_realm), headers=headers, json=payload, verify=False)
        return json.loads(response.text)['access_token'], json.loads(response.text)['refresh_token']
    except Exception as e:
        raise e
    
def agregar_usuario(in_access_token, in_new_user, in_new_pass, in_new_user_realm):
    try:
        payload= {
            "username": in_new_user,
            "enabled": "true",
            "credentials": [{
                "type": "password",
                "value": in_new_pass
            }]
        }
        headers = {
            'Authorization': 'Bearer '+ in_access_token,
            'Content-Type': 'application/json'
        }
        response = requests.post(LISTA_URLs[1].replace("<realm>", in_new_user_realm), headers=headers, json=payload)
        if (response.status_code==201):
            return 200
        elif (response.status_code==409):
            return 400
    except Exception as e:
        return e

def obtener_cliente_id(in_access_token, in_custom_realm):
    try:
        headers = {
            'Authorization': 'Bearer '+ in_access_token,
            'Content-Type': 'application/json'
        }
        response = requests.get(LISTA_URLs[2].replace("<realm>", in_custom_realm), params=headers)
        if (response.status_code==201):
            return response
        elif (response.status_code==409):
            return 400
    except Exception as e:
        return e

def agregar_cliente(in_access_token, in_new_client, in_custom_realm):
    try:
        payload= { 
            "clientId":in_new_client,
            "name":in_new_client
        }
        headers = {
            'Authorization': 'Bearer '+ in_access_token,
            'Content-Type': 'application/json'
        }
        response = requests.post(LISTA_URLs[2].replace("<realm>", in_custom_realm), headers=headers, json=payload)
        if (response.status_code==201):
            return 200
        elif (response.status_code==409):
            return 400
    except Exception as e:
        return e

def agregar_realm(in_access_token, in_new_realm):
    try:
        payload= { 
            "realm":str(in_new_realm),
        }
        headers = {
            'Authorization': 'Bearer '+ in_access_token,
            'Content-Type': 'application/json'
        }
        response = requests.post(url=LISTA_URLs[3], headers=headers, json=payload)
        if (response.status_code==201):
            return 200
        else:
            return "Error getting token"
    except Exception as e:
        return e

def obtener_cliente_secret(in_access_token, in_client, in_custom_realm, in_id):
    try:
        payload= { 
            "clientId":in_client,
            "name":in_client
        }
        headers = {
            'Authorization': 'Bearer '+ in_access_token,
            'Content-Type': 'application/json'
        }
        CLIENT_SECRET_URL = CLIENT_SECRET_URL.replace("<realm>", in_custom_realm)
        CLIENT_SECRET_URL.replace("<id>", in_id)
        response = requests.post(LISTA_URLs[4], headers=headers, json=payload)
        if (response.status_code==201):
            return 200
        elif (response.status_code==409):
            return 400
    except Exception as e:
        return e    

# LogIn
in_access_token, refresh_token = login_get_token_keycloak("admin", "4dm1n", "master", "admin-cli", "password")

# Agregar REALMS
agregar_realm(in_access_token, "cc_realm")

# Agregar cc_cliente
agregar_cliente(in_access_token, "cc_cliente", "cc_realm")

# Obtener secret del cliente
#print(obtener_cliente_secret(in_access_token, "cc_cliente", "cc_realm", "cc_cliente"))

# ADD cc_cloud_user1
agregar_usuario(in_access_token, "cc_cloud_user1", "cc_cl0ud_p455", "cc_realm")

# ADD cc_cloud_user2
agregar_usuario(in_access_token, "cc_cloud_user2", "cc_cl0ud_p455", "cc_realm")

# {
#     client_id : <my-client-name>
#     grant_type : refresh_token
#     refresh_token: <my-refresh-token>
# }