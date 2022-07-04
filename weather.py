import requests as re
import urllib.parse

address = 'tehran'
url = 'https://nominatim.openstreetmap.org/search/' + urllib.parse.quote(address) +'?format=json'

response = re.get(url).json()
lat = response[0]['lat']
long = response[0]['lon']
url2 = 'https://api.openweathermap.org/data/2.5/weather?lat=%s&lon=%s&appid=dfc43f517f1994091fa59846428d7f50' %(lat,long)

r = re.get(url2)
print(r.json()['weather'][0]['description'])
