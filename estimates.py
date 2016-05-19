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
        self.auth = {'Authorization': 'Bearer ' + config.lyftToken}

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

