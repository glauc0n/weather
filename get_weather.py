import requests

'''
Weather API Call and Local Data Storage 
'''

user = 'Benj'
api_key = '0221d3625c077e16cf35ed3e8bf6c102'
city = 'Lansing'


def get_weather(city):
    api_key = '0221d3625c077e16cf35ed3e8bf6c102'
    api_address = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'
    r = requests.get(f'{api_address}')
    print(r)
    return r.json()

