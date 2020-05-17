import requests
from pprint import pprint

city = input('City Name :')
url = 'http://api.openweathermap.org/data/2.5/weather?appid=8c888103bd9e2d03c5ed6242816a38df&q={}'.format(city)
json_data = requests.get(url).json()
#pprint(json_data)
pprint(json_data['weather'][0]['description'])

print('\n')
pprint(json_data['wind'])