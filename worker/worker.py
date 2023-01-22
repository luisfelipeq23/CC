import subprocess
import os

def download_repo(repo_url):
    try:
        repo_name = repo_url.split("/")[-1]
        if not os.path.exists(repo_name):
            os.makedirs(repo_name)
        subprocess.run(["git", "clone", repo_url, repo_name])
    except Exception:
        print('Error downloading the repository')

url = 'https://github.com/CloudComputingMasterProyecto/CC.git'
