from django.apps import AppConfig


class BerkeleyConfig(AppConfig):
    name = 'berkeley'

    def ready():
        import schedule_weather
        schedule_weather.start()
