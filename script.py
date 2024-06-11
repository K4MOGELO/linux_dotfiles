import os
import shutil
import subprocess

config_items = {
    'i3wm/config': '~/.config/i3/config',
    'i3wm/i3status.conf': '~/.config/i3status/config',
    'lf': '~/.config/lf',
    'others/.xprofile': '~/.xprofile',
    'shell/.bashrc': '~/.bashrc',
    'shell/.zshrc': '~/.zshrc',
}

config_items = {key: os.path.expanduser(value) for key, value in config_items.items()}

repo_base_path = os.path.dirname(os.path.abspath(__file__))

def copy_items():
    for dest, src in config_items.items():
        dest_path = os.path.join(repo_base_path, dest)
        src_path = os.path.abspath(src)
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

def push_to_github():
    try:
        os.chdir(repo_base_path)
        subprocess.run(['git', 'add', '.'], check=True)
        subprocess.run(['git', 'commit', '-m', 'Update configuration files'], check=True)
        subprocess.run(['git', 'push'], check=True)
        print("Changes pushed to GitHub successfully")
    except subprocess.CalledProcessError as e:
        print(f"An error occurred: {e}")

if __name__ == '__main__':
    copy_items()
    push_to_github()

