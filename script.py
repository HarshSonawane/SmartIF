import requests
import json

r = requests.get('http://api.openweathermap.org/data/2.5/weather?q=pune&appid=4190e8f33d3dcb5489def02c650faaea')
j = r.json()
data = json.loads(r)

print(data)
print(j['coord',['lon']])