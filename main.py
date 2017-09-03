import json
import requests

# Power all lights to :power: and print status code
def powerOnAll(power):
    base_url = 'http://192.168.2.22/api/MhMITSZ9EgJ2z45790rlMTZi02sXlznW82AP6Yln/'
    lights_get = requests.get(base_url + 'lights')
    lights = lights_get.json()
    payload = json.dumps({'on': power})

    powerText = 'off'
    if power == True:
        powerText = 'on'
    print('\n--- Power ' + powerText + ' ---')

    for lightId in lights:
        light = lights[lightId]
        url = base_url + 'lights/' + lightId + '/state'
        light_put = requests.put(url, data=payload)

        print( str(light['name']) + ': ' + str(light_put.status_code) )

# Print light names + current power status
def printLightInfo():
    base_url = 'http://192.168.2.22/api/MhMITSZ9EgJ2z45790rlMTZi02sXlznW82AP6Yln/'
    lights_get = requests.get(base_url + 'lights')
    lights = lights_get.json()

    print('\n--- Light Status ---')

    for lightId in lights:
        light = lights[lightId]
        powerText = 'off'
        if light['state']['on'] == True:
            powerText = 'on'

        print( str(light['name']) + ': ' + powerText )


if __name__ == '__main__':
    #username: MhMITSZ9EgJ2z45790rlMTZi02sXlznW82AP6Yln
    powerOnAll(False)
    #powerOnAll(True)
    printLightInfo()
