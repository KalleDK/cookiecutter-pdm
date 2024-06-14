import sys
import subprocess
import pathlib
import json

def update_from_git():
    result = subprocess.run(["git", "config", "user.name"], capture_output=True, check=True)
    user_name = result.stdout.decode().strip()
    result = subprocess.run(["git", "config", "user.email"], capture_output=True, check=True)
    user_email = result.stdout.decode().strip()

    config_path = pathlib.Path("cookiecutter.json")
    with config_path.open() as fp:
        config = json.load(fp)
    config["author_name"] = user_name
    config["author_mail"] = user_email
    with config_path.open("w") as fp:
        json.dump(config, fp)
   

if __name__ == "__main__":
    update_from_git()