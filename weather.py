import requests;
from datetime import datetime;

api_key = 'a315eff5dff799c14d39395b7e117ef7' 

location = input("Enter the city Name : ");

complete_api_link = "https://api.openweathermap.org/data/2.5/weather?q="+location+"&appid="+api_key+""; 

api_link = requests.get(complete_api_link);

api_data =  api_link.json();

temp_city  =((api_data['main']['temp'])- 273.15);
weather_desc = api_data['weather'][0]['description']
hmdt = api_data['main']['humidity'] 
wind_spd = api_data['wind']['speed']
date_time = datetime.now().strftime("%d %b %Y | %I:%M:%S $p") 

with open('weather_report.txt','wb') as f:

    f.write(api_link.content); 

print("---------------------------------------------------------------------");
print("Weather status for - {} || {}".format(location.upper(), date_time));
print("---------------------------------------------------------------------");


print("Current temperature is       : {:.2f} deg C".format(temp_city));
print("Current weather Desc         :", weather_desc);
print("Current humidity             :",hmdt,'%');
print("Current wind Speed           :",  wind_spd,'kmph');