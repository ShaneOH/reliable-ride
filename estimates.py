import requests as req
import json
import config

class Uber:
    url = 'https://api.uber.com/v1/estimates'
    
    def __init__(self):
        self.auth = {'Authorization': 'Token ' + config.uberToken}

class Lyft:
    url = 'https://api.lyft.com/v1'

    def __init__(self):
        self.auth = self.getToken()

    def getToken(self):
        i = 1;      

class Estimate:
    lyftUrl = 'https://api.lyft.com/v1'
    lyftAuth = {'Authorization': 'Bearer ' + config.token}
    location = {'start_latitude': lat, 'start_longitude': long}

    #r = req.get(uberUrl+'/time', headers=uberAuth, params=location)
    #uberTime = json.loads(r.text)

def main():
    print "Hello!"

if __name__ == '__main__':
    main()

