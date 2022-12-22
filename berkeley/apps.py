from django.apps import AppConfig


class BerkeleyConfig(AppConfig):
    name = 'berkeley'

    def ready(self):
        import berkeley.schedule_weather as schedule_weather
        schedule_weather.start()
