import json
import lxml
import requests

with open('config.json', 'r') as f:
    configs = json.load(f)

for config in configs:
    payload = {'userid': config['username'], 'password': config['password']}
    response = requests.post(config['url'], payload)
    content = response.content.decode('utf-8')
    with open(config['filename'], 'w') as f:
        f.write(content)
