import schedule
from utils import get_weather
import os
import time

def job():
    
    print('Running freeze warning service')
    get_weather.main()

schedule.every().day.at('06:00').do(job)

while True:
    schedule.run_pending()
    time.sleep(1)