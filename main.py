import requests
from Location import Locate
from colorama import Fore, init
import customtkinter

API_KEY = "API KEY" # OpenWeatherMap API Key


Gui = customtkinter.CTk()
Gui.geometry("400x250")
Gui.title("Weather App")

label_1 = customtkinter.CTkLabel(master=Gui,text="Loading...",font=("Courier", 18),text_color="#2ECC71")
label_1.pack(pady=20)

label_2 = customtkinter.CTkLabel(master=Gui,text="Loading...",font=("Courier", 16),text_color="#2ECC71")
label_2.pack(pady=10)

label_3 = customtkinter.CTkLabel(master=Gui,text="Loading...",font=("Courier", 16),text_color="#2ECC71")
label_3.pack(pady=10)

def WeatherChecker():
    location = Locate.get_location() # Location
    city = location["city"]

    # Unknown
    if city == "Unknown_City":
        print(Fore.RED + "Location could not be found.")
        label_1.configure(text="Location not found")

        label_2.configure(text="")

        label_3.configure(text="")
        Gui.after(10000, WeatherChecker) 
        return
    url = (
        f"https://api.openweathermap.org/data/2.5/weather" 
        f"?q={city}"   
        f"&appid={API_KEY}" # API KEY
        f"&units=metric"
        f"&lang=en"
    )

    try:
        res = requests.get(url, timeout=5)
        data = res.json()

        if res.status_code != 200:
            error_message = data.get("message","Unknown API error")
            print(Fore.RED + error_message)
            label_1.configure(text="API Error")
            label_2.configure(text=error_message)
            label_3.configure(text="")
        else:
            fcity = data["name"]
            country = data["sys"]["country"]
            temp = data["main"]["temp"]
            desc = data["weather"][0]["description"]
            print(Fore.BLUE + "Found location : " + Fore.GREEN + f"{fcity}, {country}")
            print(Fore.BLUE + "Heat : " + Fore.YELLOW + f"{temp}°C")
            print(Fore.BLUE + "Weather : " +Fore.WHITE + f"{desc}")
            label_1.configure(text=f"Location : {fcity}, {country}")
            label_2.configure(text=f"Temperature : {temp}°C")
            label_3.configure(text=f"Weather : {desc}")
    except requests.RequestException:
        print(Fore.RED + "Internet connection error.")
        label_1.configure(text="Connection Error")
        label_2.configure(text="Check your internet")
        label_3.configure(text="")
    Gui.after(10000, WeatherChecker)
WeatherChecker()
Gui.mainloop()