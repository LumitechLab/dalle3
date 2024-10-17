import os
import json
import requests
from datetime import datetime

### ENV VARS
# set env vars from json file
def set_env_vars_from_json(file_path):
  with open(file_path, 'r') as file:
    env_vars = json.load(file)

  for key, value in env_vars.items():
    os.environ[key] = value

# get dict of env vars from list
def env_vars(keys):
  return {k: os.environ[k] for k in keys}

# get value of env var
def env_var(key):
  return os.environ[key]

### TIME
def timestamp():
  return datetime.now().strftime("%Y%m%d%H%M%S")

### IMAGE DOWNLOAD
def download_image(url, file_path):
  response = requests.get(url)

  dir = os.path.dirname(file_path)
  os.makedirs(dir, exist_ok=True)

  if response.status_code == 200:
    with open(file_path, 'wb') as file:
      file.write(response.content)
    return True
  else:
    return False