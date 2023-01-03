# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
import subprocess
import requests
import os

@api_view(['GET'])
def home(request):
    return render(request, 'home.html')


@api_view(['POST'])
def download_and_execute_repo(request):
    repo_url = request.data["repo_url"]
    repo_name = repo_url.split("/")[-1]

    # Download the repository
    if not os.path.exists(repo_name):
        os.makedirs(repo_name)
    subprocess.run(["git", "clone", repo_url, repo_name])

    # Execute the main.py file in the repository
    try:
        subprocess.run(["python", f"{repo_name}/main.py"])
        return Response({"message": "Repository executed successfully."})
    except Exception as e:
        return Response({"message": str(e)}, status=500)