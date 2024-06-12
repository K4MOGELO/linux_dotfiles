import os
import shutil
import subprocess
import json

with open('config_paths.json') as f:
    config_paths = json.load(f)

config_paths = {key: os.path.expanduser(value) for key, value in config_paths.items()}
repo_base_path = os.path.dirname(os.path.abspath(__file__))

def pull_from_github():
    try:
        os.chdir(repo_base_path)
        subprocess.run(['git', 'pull'], check=True)

        print("Latest changes pulled from GitHub successfully")
    except subprocess.CalledProcessError as e:
        print(f"An error occurred while pulling changes: {e}")

def update_configurations():
    for src, dest in config_paths.items():
        src_path = os.path.join(repo_base_path, src)
        dest_path = os.path.abspath(dest)
        os.makedirs(os.path.dirname(dest_path), exist_ok=True)

        if os.path.exists(src_path):
            if os.path.isdir(src_path):
                if os.path.exists(dest_path):
                    shutil.rmtree(dest_path)
                shutil.copytree(src_path, dest_path)
                print(f"Copied directory {src_path} to {dest_path}")
            else:
                shutil.copy2(src_path, dest_path)
                print(f"Copied file {src_path} to {dest_path}")
        else:
            print(f"Source {src_path} does not exist")

if __name__ == '__main__':
    pull_from_github()
    update_configurations()

