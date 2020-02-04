from pymongo import MongoClient
from datetime import datetime

import api_call

cluster = MongoClient('mongodb+srv://gloucon:test@clusto-oslu1.mongodb.net/test?retryWrites=true&w=majority')

db = cluster['Test']
collection = db['Test']

now = datetime.now()
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")

weather_data = api_call.get_weather('San Francisco')
location = weather_data['name']
weather_data["_id"] = f'{location} {dt_string}'

collection.insert_one(weather_data)

#git test


