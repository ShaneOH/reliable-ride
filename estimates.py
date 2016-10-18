import requests as req
import json, os, csv

with open('config.json', 'r') as f:
    config = json.load(f)

#token does not expire
uber = {'url': 'https://api.uber.com/v1/estimates/time', 'auth': {'Authorization': 'Token ' + config['uberToken']}}
#token expires every hour
lyft = {'url': 'https://api.lyft.com/v1/eta'}

def main():
    authLyft()
    with open(os.path.join(os.path.dirname(__file__), './data/places.csv')) as places:
        for place in csv.reader(places, delimiter = ','):
            lyftTime = etaLyft(place)
            uberTime = etaUber(place)

def authLyft():
    headers = {'Content-Type': 'application/json'}
    data = '{"grant_type": "client_credentials", "scope": "public"}'
    r = req.post('https://api.lyft.com/oauth/token', headers=headers, data=data, auth=(config['lyftID'], config['lyftSecret']))
    token = json.loads(r.text)
    lyft['auth'] = {'Authorization': 'Bearer ' + token['access_token']}

def etaLyft(place):
    location = {'lat': place[2], 'lng': place[3]}
    r = req.get(lyft['url'], headers=lyft['auth'], params=location)
    return json.loads(r.text)

def etaUber(place):
    location = {'start_latitude': place[2], 'start_longitude': place[3]}
    r = req.get(uber['url'], headers=uber['auth'], params=location)
    return json.loads(r.text)

if __name__ == '__main__':
    main()
   

