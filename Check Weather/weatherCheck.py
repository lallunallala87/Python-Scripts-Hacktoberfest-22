

import requests

api_key = "1d893f1f78b7ba5b746b1b654f565b39"
base_url= "http://api.openweathermap.org/data/2.5/weather?"

city_name = input("Enter city name : ") 
full_url = base_url + "q=" + city_name + "&appid=" + api_key
req = requests.get(full_url)
info = req.json() 

if info["cod"] != "404": 
    x = info["main"] 
    current_temperature = x["temp"]
    tnc = round(float(current_temperature - 273.15),2)
    current_pressure = x["pressure"] 
    current_humidiy = x["humidity"] 
    z = info["weather"] 
    weather_description = z[0]["description"]
    s = info["wind"]
    speed = s["speed"]
    print()
    print("Temperature (in celsius unit): ", 
                  round(float(current_temperature - 273.15),2) , "°C",
            "\nAtmospheric pressure : " +
                  str(round(current_pressure*0.029529)) + "hg"
            "\nHumidity : " +
                  str(current_humidiy) + "%"
            "\nDescription: " +
                  str(weather_description).capitalize()+
                "\nWind Speed :" + str(round(speed*(18/5))) + "km/hr")

else: 
  print(" City Not Found ")