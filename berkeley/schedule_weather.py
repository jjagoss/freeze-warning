import schedule
from utils import get_weather
import os
import time
from apscheduler.schedulers.background import BackgroundScheduler


def start():
    scheduler = BackgroundScheduler()
    scheduler.add_job(get_weather.main, 'interval', days=1)
    scheduler.start()