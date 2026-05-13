import requests
import weather
from Location import Locate
from colorama import Fore, Back, Style, init
## import customtkinter

API_KEY = "Enter your API key here"
                    ## Enter your API key here.
def WeatherChacker():
    while 1:                                               ## API keys can sometimes take up to 10 minutes to process.
        city = Locate.city                              ## You can obtain your keys from https://home.openweathermap.org/api_keys

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
            weather.Bye1() ## While loop output
            break
        elif res.status_code != 200:
            print(Fore,RED , f"Error: {data.get('Error message !!!', 'Unknown city or country !!!')}") ## Error messages are not detailed
        else:
            fcity = data["name"]
            country = data["sys"]["country"]
            temp = data["main"]["temp"]
            desc = data["weather"][0]["description"]
            print(Fore.BLUE ,"Found location :", Fore.GREEN , f"{fcity}, {country}")   ## There might be some changes in the city name. The result is correct.
            print(Fore.BLUE , "Heat :          ",Fore.YELLOW ,f"{temp}°C")          ## You can modify the results section to suit your own language.
            print(Fore.BLUE , "Weather :       ",Fore.WHITE,f"{desc}")       ## I know I could have done it differently instead of leaving spaces, but to be honest, I was too lazy :D
            break
WeatherChacker()

## 
