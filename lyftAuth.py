import requests as req
import json

with open('config.json', 'r') as f:
    config = json.load(f)

headers = {'Content-Type': 'application/json'}
data = '{"grant_type": "client_credentials", "scope": "public"}'
r = req.post('https://api.lyft.com/oauth/token', headers=headers, data=data, auth=(config['lyftID'], config['lyftSecret']))
token = json.loads(r.text)
config['lyftToken'] = token['access_token']

with open('config.json', 'w') as f:
    json.dump(config, f)

