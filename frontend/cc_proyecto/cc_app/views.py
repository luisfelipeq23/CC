from django.shortcuts import render
from rest_framework.decorators import api_view
from .models import Repo
from .forms import RepoForm

def home(request):
    return render(request, 'home.html')

def download_repo(request):
    form = RepoForm()
    if request.method == 'POST':
        form = RepoForm(request.POST)
        if form.is_valid():
            repo_name=form.cleaned_data['repo_name']
            repo_url=form.cleaned_data['repo_url']
            archivo=form.cleaned_data['archivo']
            repo = Repo(repo_name, repo_url, archivo)
            repo.save()
            return render(request, 'RepoForm.html', {'form': RepoForm()})
        return render(request, 'RepoForm.html', {'form': form, "error": "Completar los datos requeridos"})
    return render(request, 'RepoForm.html', {'form': form})
