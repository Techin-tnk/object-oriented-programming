import requests

api_key = "b44b7edfc716b6c7309e2f11047d8d81"
city = "bangkok"
url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
url_json = "https://api.openweathermap.org/data/2.5/weather?q=bangkok&appid=b44b7edfc716b6c7309e2f11047d8d81"

result = requests.get(url).json()
# print(result)   
city = result['name']
country = result ['sys']['country']
weather = result ['weather'][0]['main']
description = result ['weather'][0]['description']
temp = result ['main']['temp'] -273.15

print(f'เมือง:{city} ประเทศ: {country}')
print(f'สภาพอากาศวันนี้: {weather} มีลักษณะ:{description}')
print(f'อุณภูมิตอนนี้: {temp} C')