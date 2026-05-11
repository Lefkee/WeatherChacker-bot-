import requests
import weather

API_KEY = "781092038dfc8d84fc12db9e1bb2d856"
                    ## Enter your API key here.
def WeatherChacker():
    while 1:                                               ## API keys can sometimes take up to 10 minutes to process.
        city = input("Enter city name : ")                      ## You can obtain your keys from https://home.openweathermap.org/api_keys

        url = (
            f"https://api.openweathermap.org/data/2.5/weather"
            f"?q={city}"
            f"&appid={API_KEY}"
            f"&units=metric"
            f"&lang=en" ## To change the language, you need to modify this section to change the output;
        )               ## to change the remaining parts, you need to modify the parts in the normal rows.

        res = requests.get(url)
        data = res.json()

        if city == "0":
            weather.Bye1()
            break
        elif res.status_code != 200:
            print(f"Error: {data.get('Error message', 'İdk :D')}")
        else:
            fcity = data["name"]
            country = data["sys"]["country"]
            temp = data["main"]["temp"]
            desc = data["weather"][0]["description"]
            print(f"\nFound location : {fcity}, {country}")   ## There might be some changes in the city name. The result is correct.
            print(f"Heat : {temp}°C")          ## You can modify the results section to suit your own language.
            print(f"Weather : {desc}")
WeatherChacker()