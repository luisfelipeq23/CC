from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework import viewsets
from rest_framework.response import Response
from .models import Repo
from .forms import RepoForm
from .kafka_prod import kafka_productor
from cc_proyecto import serializers as ser

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
            kafka_prod = kafka_productor(repo_name, repo_url, "pendientes")
            kafka_prod.enviar_mensaje_kafka()
            return render(request, 'RepoForm.html', {'form': RepoForm()})
        return render(request, 'RepoForm.html', {'form': form, "error": "Complete los datos requeridos"})
    return render(request, 'RepoForm.html', {'form': form})

# class RepoViewSet(viewsets.ViewSet):
#     def list(self, request): #/api/repos
#         repos = Repo.objects.all()
#         serializer = ser.RepoSerializer(repos, many=True)
#         return Response(serializer.data)

#     def create(self, request): # /api/repos
#         pass

#     def retreive(self, request, pk=None): # /api/products/<str:id>
#         pass

#     def update(self, request, pk=None): # /api/products/<str:id>
#         pass

#     def destroy(self, request, pk=None): # /api/products/<str:id>
#         pass