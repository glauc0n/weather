import get_weather
import mongo

city = 'San Francisco'

weather_data = get_weather.get_weather(city)

mongo.m_push(weather_data)

