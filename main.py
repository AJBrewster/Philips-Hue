import json
import requests

def powerOnAll(power):
    base_url = 'http://192.168.2.22/api/MhMITSZ9EgJ2z45790rlMTZi02sXlznW82AP6Yln/'
    lights_get = requests.get(base_url + 'lights')
    lights = lights_get.json()
    payload = json.dumps({'on': power})

    # [{'error': {'type': 2, 'description': 'body contains invalid json', 'address': '/2/state'}}]
    # could be something wrong with :payload: or :url:
    for light in lights:
        url = base_url + 'lights/' + light + '/state'
        light_put = requests.put(url, data=payload)
        print(light_put.json())

def printLightInfo():
    base_url = 'http://192.168.2.22/api/MhMITSZ9EgJ2z45790rlMTZi02sXlznW82AP6Yln/'
    lights_request = requests.get(base_url + 'lights')
    lights = lights_request.json()

    for light in lights:
        name = lights[light]['name']
        state = lights[light]['state']
        print( str(name) + ': ' + str(state['on']) )


if __name__ == '__main__':
    print('\n--- Power On ---')
    powerOnAll(True)
    print('\n--- Light Information ---')
    printLightInfo()
