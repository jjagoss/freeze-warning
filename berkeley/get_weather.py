import requests
import json
import os
import pandas as pd
from django.conf import settings
from django.core.mail import send_mail
from .models import Subscriber
os.environ['DJANGO_SETTINGS_MODULE'] = 'weather.settings'

berkeley_lat = 37.8715
berkeley_long = -122.2730

def get_weather(lat, long):

    metadata_url = f"https://api.weather.gov/points/{lat},{long}"

    w_metadata = requests.get(metadata_url)

    forecast_url = w_metadata.json()['properties']['forecastHourly']

    forecast = requests.get(forecast_url)
    
    hourly_forecast = forecast.json()['properties']['periods']

    return hourly_forecast

def get_data(hourly_forecast):

    periods = []
    dates = []
    temps = []
    descriptions = []

    for hour in hourly_forecast:
        periods.append(hour['number'])
        dates.append(hour['startTime'])
        temps.append(hour['temperature'])
        descriptions.append(hour['shortForecast'])

    weather_df = pd.DataFrame({'periods': periods,
                            'dates': dates,
                            'temps': temps,
                            'descriptions': descriptions})
    return weather_df

def clean_data(weather_df):
    
    weather_df['dates'] = pd.to_datetime(weather_df['dates'])
    weather_df['day'] = weather_df['dates'].dt.date

    result = weather_df.groupby('day').temps.mean().head(3).mean()

    return result

def send_email(result):

    result_message = f"the average temperature over the next 3 days in Berkeley will be {result}, degrees Farenheit"

    send_mail(
        subject='Test of weather app',
        message=result_message,
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=Subscriber.objects.values_list('email_address', flat=True),
        fail_silently=False,
    )

def main(lat=berkeley_lat, long=berkeley_long):

    hourly_forecast = get_weather(lat=lat, long=long)
    weather_df = get_data(hourly_forecast=hourly_forecast)
    result = clean_data(weather_df=weather_df)
    send_email(result=result)
