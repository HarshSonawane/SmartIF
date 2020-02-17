import requests

api_key = '4190e8f33d3dcb5489def02c650faaea'

def get_wheather(city):
    try:
        url = 'api.openweathermap.org/data/2.5/weather'
        params = {'city': city, 'appid': api_key}
        r = requests.get(url, params=params)
        cords = r.json()
        return r.json()
    except :
        print('passed')
        pass