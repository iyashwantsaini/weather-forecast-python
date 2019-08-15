import requests
from random import choice
from pyfiglet import figlet_format
from termcolor import colored

header=figlet_format('Weather')
header=colored(header,color='magenta')
print(header)

user_input=input('Enter the state : ')
url='http://api.openweathermap.org/data/2.5/forecast?q='+user_input+'&APPID=b83f69aa85641833c72ee4fa6fd89378'
req=requests.get(
    url,
    headers={'Accept':'application/json'},
    params={'term':user_input}
).json()

for i in range(0,20,2):
    print('date/time '+req['list'][i]['dt_txt']+ ' \n main : '+req['list'][i]['weather'][0]['main'] +' \n '+'description : '+req['list'][i]['weather'][0]['description'])




# Example of using API key in API call
# Description:
# Please, use your API key in each API call.
# We do not process API requests without the API key.
# API call:
# http://api.openweathermap.org/data/2.5/forecast?id=524901&APPID={APIKEY}
# Parameters:
# APPID {APIKEY} is your unique API key 
# Example of API call:
# api.openweathermap.org/data/2.5/forecast?id=524901&APPID=1111111111