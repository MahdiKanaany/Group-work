try:
    import requests as re
    import urllib.parse
    from googletrans import Translator, constants
    translator = Translator()
    address = input('Please give me your city: ')
    url = 'https://nominatim.openstreetmap.org/search/' + urllib.parse.quote(address) +'?format=json'
    response = re.get(url).json()
    lat = response[0]['lat']
    long = response[0]['lon']
    url2 = 'https://api.openweathermap.org/data/2.5/weather?lat=%s&lon=%s&appid=dfc43f517f1994091fa59846428d7f50' %(lat,long)
    r = re.get(url2)
    country = r.json()['sys']['country']
    temp_min = (r.json()['main']['temp_min'])-273.15
    temp_max = (r.json()['main']['temp_max'])-273.15                        
    w = r.json()['weather'][0]['description']
    name = r.json()['name']
    translation = translator.translate(w, dest="fa")
    print(name,'in',country,'country')
    print(translation.text)
    print('حداقل دما:',temp_min,'و حداکثر دما:',temp_max)
except:
    print('''Please connect to the internet.
If you are connected to the internet please check the city.''')

