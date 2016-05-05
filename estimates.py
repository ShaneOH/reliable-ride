import requests as req
import json
import config

url = 'https://api.uber.com/v1/estimates'
lat = '40.740308'
long = '-73.985428'
headers = {'Authorization': 'Token ' + config.token}
location = {'start_latitude': lat, 'start_longitude': long}

r = req.get(url+'/time', headers=headers, params=location)
estimates = json.loads(r.text)

