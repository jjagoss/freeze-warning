from django.db import models

# Create your models here.
class Subscriber(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email_address = models.CharField(max_length=100)

    def __str__(self):
        return self.email_address