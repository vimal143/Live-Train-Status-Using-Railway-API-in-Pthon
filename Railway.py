import requests
import sys
from datetime import datetime

#Enter Train Number
trainNumber=input("Enter train Number:")
#Your Journey Station Code-EX(BSB for Varanasi and NDLS for New Delhi)
stnCode=input("Enter station Code:")
#Today's Date automatically taken from System
today=datetime.today().strftime('%d-%m-%Y')
#Railway API. Replace 'Your API key' with API key you get from https://railwayapi.com

#URL for getting Train Name from Number entered
trnNameUrl=f'https://api.railwayapi.com/v2/name-number/train/{trainNumber}/apikey/Your API KEY/'
name=requests.get(trnNameUrl)
nameResult=name.json()

#URL for getting Live Status
url=f'https://api.railwayapi.com/v2/live/train/{trainNumber}/station/{stnCode}/date/{today}/apikey/YOUR API KEY/'
res=requests.get(url)
data=res.json()
scharr=data['status']['scharr']
schdep=data['status']['schdep']
actarr=data['status']['actarr']
actdep=data['status']['actdep']
trnName=nameResult['train']['name']
print(data['position'])
print(trnName)
print('Scheduled Arriavl:   ',scharr)
print("Scheduled Departure:   ",schdep)
print("Actual Arrival:   ",actarr)
