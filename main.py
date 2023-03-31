import requests
import time
from pygame import mixer
import time

flag = False

pathToSound = "./path-to-sound-file"                                       # path to sound file (mp3)
priceLimit = 25000                                          # The price limit after which the alarm will sound
alarmCount = 0                                              # Initial alarm count
maxAlarms = 3                                               # amount of alarms after reaching limit
URL = "https://api.coinbase.com/v2/prices/BTC-USD/spot"     # URL to coinbase

while(flag != True):   
    btcUsd = requests.get(URL)
    btcGbp = requests.get(URL)
    
    # BTC / USD
    price_usd = btcUsd.json() ["data"]["amount"]

    # BTC / GBP
    price_gpb = btcGbp.json()["data"]["amount"]

     # PRINT-OUT
    print ("BTC/USD: " + price_usd + "\n" + "BTC/GBP: " + price_gpb)

    if(alarmCount != maxAlarms):
        alarmCount += 1 
        try:
            if(float(price_usd) > 25000):
                mixer.init()
                mixer.music.load(pathToSound) 
                mixer.music.play()
                while mixer.music.get_busy():
                    time.sleep(1)
        except(FileNotFoundError):
            print("File not found, proceeding with no alarm...")
    time.sleep(4)  




    
   