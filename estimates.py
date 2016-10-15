import requests as req
import json, sys, os, csv

with open('config.json', 'r') as f:
    config = json.load(f)

uber = {'url': 'https://api.uber.com/v1/estimates/time'};
lyft = {'url': 'https://api.lyft.com/v1/eta'};

def main():
    authLyft()
    authUber()
    with open(os.path.join(os.path.dirname(__file__), './data/places.csv')) as places:
        for place in csv.reader(places, delimiter = ','):
            location = {'start_latitude': place[2], 'start_longitude': place[3]}


def authLyft():
    headers = {'Content-Type': 'application/json'}
    data = '{"grant_type": "client_credentials", "scope": "public"}'
    r = req.post('https://api.lyft.com/oauth/token', headers=headers, data=data, auth=(config['lyftID'], config['lyftSecret']))
    token = json.loads(r.text)
    lyft['token'] = token['access_token']

def authUber():
    pass

def etaLyft():
    pass

def etaUber():
    pass

if __name__ == '__main__':
    main()
   

