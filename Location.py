import requests

class Locate:
    _data = requests.get('http://ip-api.com/json/').json()
    
    country = _data.get('country', 'Unknown_Country')
    city = _data.get('city', 'Unknown_City')
    ip = _data.get('query', '0.0.0.0')
