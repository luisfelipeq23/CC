import git
import subprocess
import requests
import os

def download_repo(repo_url):
    try:
        repo_name = repo_url.split("/")[-1]
        if not os.path.exists(repo_name):
            os.makedirs(repo_name)
        subprocess.run(["git", "clone", repo_url, repo_name])
    except Exception:
        print('Error downloading the repositorie')

def execute_repo(repo_url):
    try:
        repo_name = repo_url.split("/")[-1]
        subprocess.run(["python", f"{repo_name}/main.py"])
    except Exception:
        print('Error downloading the repositorie')

def download_and_execute_repo(request):
    repo_url = request.POST["repo_url"]
    download_repo(repo_url)
    execute_repo(repo_url)