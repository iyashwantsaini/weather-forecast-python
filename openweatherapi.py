import requests
from random import choice
from pyfiglet import figlet_format
from termcolor import colored

header=figlet_format('Weather')
header=colored(header,color='magenta')
print(header)

user_input=input('Enter the state : ')
# Enter your key here in the url
url='http://api.openweathermap.org/data/2.5/forecast?q='+user_input+'&APPID=your_key_goes_here'
req=requests.get(
    url,
    headers={'Accept':'application/json'},
    params={'term':user_input}
).json()

for i in range(0,20,2):
    print('date/time '+req['list'][i]['dt_txt']+ ' \n main : '+req['list'][i]['weather'][0]['main'] +' \n '+'description : '+req['list'][i]['weather'][0]['description'])



# openweatherapi intructions : 
    
# Example of using API key in API call
# Please, use your API key in each API call.
# API call:
# http://api.openweathermap.org/data/2.5/forecast?id=524901&APPID={APIKEY}
# Parameters:
# APPID {APIKEY} is your unique API key 
# Example of API call:
# api.openweathermap.org/data/2.5/forecast?id=524901&APPID=1111111111
