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
        DATA_DICT.append(container_name,container_ip_address)
        print(container_name + " " + "cc_backend" + " " + container_ip_address)
