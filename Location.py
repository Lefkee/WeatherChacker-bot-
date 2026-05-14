import requests

class Locate:
    def get_location():
        try:
            response = requests.get("http://ip-api.com/json/",timeout=5)
            data = response.json()
            return {"country": data.get("country", "Unknown_Country"),"city": data.get("city", "Unknown_City"),"ip": data.get("query", "0.0.0.0")}
        except requests.RequestException:
            return {"country": "Unknown_Country","city": "Unknown_City","ip": "0.0.0.0"}