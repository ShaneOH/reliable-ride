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
        try:
            token = config.lyftToken
        except AttributeError:
            headers = {'Content-Type': 'application/json'}
            data = '{"grant_type": "client_credentials", "scope": "public"}'
            r = req.post('https://api.lyft.com/oauth/token', headers=headers, data=data, auth=(config.lyftID, config.lyftSecret))
            token = json.loads(r.text)
        return token

class Estimate:
    pass
    #location = {'start_latitude': lat, 'start_longitude': long}

    #r = req.get(uberUrl+'/time', headers=uberAuth, params=location)
    #uberTime = json.loads(r.text)

def main():
    lyft = Lyft()
    print lyft.auth

if __name__ == '__main__':
    main()

