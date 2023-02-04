from django.shortcuts import render
from .models import Repo
from .forms import RepoForm
import json
import os
from .kafka_producer import kafka_productor

current_path = os.path.dirname(os.path.abspath(__file__))
CLIENT_SECRET = ""
CLIENT_ID = "cc_cliente"

file = current_path + "/login_data.json"

with open(file, "r") as file:
    data = json.load(file)
    CLIENT_ID = data["client_id"]
    CLIENT_SECRET = data["client_secret"]

def home(request):
    return render(request, 'home.html')

def download_repo(request):
    form = RepoForm()
    if request.method == 'POST':
        form = RepoForm(request.POST)
        if form.is_valid():
            repo_url=form.cleaned_data['url_repo']
            repo = Repo(url_repo=repo_url)

            # Salvar repositorio a BD
            repo.save()
            
            # Envío de mensaje a Kafk""
            kafka_prod = kafka_productor(repo_url, "pendientes", "cc_kafka:9092")
            kafka_prod.enviar_mensaje_kafka()
            return render(request, 'RepoForm.html', {'form': RepoForm()})
        return render(request, 'RepoForm.html', {'form': form, "error": "Complete los datos requeridos"})
    return render(request, 'RepoForm.html', {'form': form})

# def login(request):
#     if request.method == 'POST':
#         payload = {
#             "username": request.POST.get('username'),
#             "password": request.POST.get('password'),
#             "grant_type": "password",
#             "client_id": CLIENT_ID,
#             "client_secret": CLIENT_SECRET
#         }
#         headers = {
#             'Content-Type': 'application/x-www-form-urlencoded'
#         }
#         response = l.login(url="http://localhost:8080/realms/master/protocol/openid-connect/token", clientid="cc_cliente", ealm="cc_realm", cliente_secret="")
#         response = requests.post("http://0.0.0.0:8080/realms/cc_realm/protocol/openid-connect/token", json=payload, headers=headers)
#         if response.status_code == 200:
#             token = response.json().get("access_token")
#             request.session['keycloak_token'] = token
#             return render(request, ("RepoForm.html"))
#         else:
#             # handle the error
#             pass
#     return render(request, "login.html")
