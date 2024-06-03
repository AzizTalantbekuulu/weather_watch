from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    ROLE_CHOICES = (
        ('admin', 'Admin'),
        ('user', 'User'),
    )
    role = models.CharField(max_length =100, choices=ROLE_CHOICES)
    REQUIRED_FIELDS =['role']


class Sensor(models.Model):
    SENSOR_TYPES = [
        ('temp', 'Temperature'),
        ('humid', 'Humidity'),
        ('wind', 'Wind Speed'),
    ]

    sensor_id = models.AutoField(primary_key=True)
    type = models.CharField(max_length=100, choices=SENSOR_TYPES)
    model = models.CharField(max_length=100)
    installation_data = models.DateField(auto_now=False, auto_now_add=True)
    status = models.CharField(max_length=10)


class Data(models.Model):
    data_id = models.AutoField(primary_key=True)
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    humidity = models.FloatField(null=True, blank=True)
    wind_speed = models.FloatField(null=True, blank=True)
    temperature = models.FloatField(null=True, blank=True)
    pressure = models.FloatField(null=True, blank=True)


class Alert(models.Model):
    alert_id = models.AutoField(primary_key=True)
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    description = models.TextField()

