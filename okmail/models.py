from django.db import models
from datetime import datetime
from django.db.models.signals import post_save
from django.dispatch import receiver
from . import views
import requests
import os

# for env variable
from dotenv import load_dotenv
load_dotenv()


# env variable
weather_api_key = os.environ.get("weather_api_key")

# Create your models here.
class MailRecord(models.Model):
    Mumbai = 'Mumbai'
    Delhi = 'Delhi'
    Chennai = 'Chennai'
    Banglore = 'Banglore'
    Kolkata = 'Kolkata'
    INDIAN_CITIES = [
        (Mumbai, 'Mumbai'),
        (Delhi, 'Delhi'),
        (Banglore, 'Banglore'),
        (Kolkata, 'Kolkata'),
        (Chennai, 'Chennai'),
    ]
    username = models.CharField(max_length=50,null=False)
    email = models.EmailField(null=False)
    city_name = models.CharField(max_length=20,null=False, choices=INDIAN_CITIES)

    def __str__(self) -> str:
        return self.email


@receiver(post_save, sender=MailRecord)
def send_mail(sender, instance, created, **kwargs):
    if created:
        email = instance.email
        city = instance.city_name

        # subject to send 
        email_subject = 'Hi {}, interested in our services'.format(instance.username)
        try:
            response = requests.get('http://api.openweathermap.org/data/2.5/weather?q={}&appid={}'.format(city, weather_api_key), timeout=5)
            if response.status_code == 200:
                print(response.json())
                json_respnse = response.json()
                current_temp = round(json_respnse.get('main').get('temp') - 273.15, 2)
                views.mail_het_send(email_subject, current_temp, email)
                    
                print(response.status_code)
            
        except:
            print('exception in models.py')