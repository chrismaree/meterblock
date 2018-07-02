# basic script to retrieve power consumed by sonoff POW from HTTP
import requests

url = 'http://10.0.0.41/cm?cmnd='
command = 'Status%208'

response = requests.post(url+command)
print (response.json()['StatusSNS']['ENERGY']['Power'])