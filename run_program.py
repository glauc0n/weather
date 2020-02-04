import api_call
import mongodb

city = 'San Francisco'

weather_data = api_call.get_weather(city)

mongodb.mongo_push(weather_data)
