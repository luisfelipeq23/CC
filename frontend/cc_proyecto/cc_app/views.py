from django.shortcuts import render
from rest_framework.decorators import api_view
from .models import Repo
from .forms import RepoForm

from kafka import KafkaProducer

def home(request):
    return render(request, 'home.html')

def download_repo(request):
    form = RepoForm()
    if request.method == 'POST':
        form = RepoForm(request.POST)
        if form.is_valid():
            repo_name=form.cleaned_data['nombre_repo']
            repo_url=form.cleaned_data['url_repo']
            repo = Repo(nombre_repo=repo_name, url_repo=repo_url)
            # Salvar repositorio a BD
            repo.save()
            # Envío de mensaje a Kafka
            enviar_mensaje_kafka(repo_name, repo_url, "pendientes")
            return render(request, 'RepoForm.html', {'form': RepoForm()})
        return render(request, 'RepoForm.html', {'form': form, "error": "Complete los datos requeridos"})
    return render(request, 'RepoForm.html', {'form': form})

def enviar_mensaje_kafka(repo_name, repo_url, topic):
    mensaje = {repo_name:repo_url}
    productor = KafkaProducer(bootstrap_servers="cc_kafka:9092")
    productor.send(topic, mensaje)
