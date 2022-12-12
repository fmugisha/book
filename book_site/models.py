from django.db import models

# Create your models here.
class User(models.Model):
    firstName = models.CharField(max_length=100)
    secondName = models.CharField(max_length=100)
    gender = models.CharField(max_length=10)
    phoneNumber = models.IntegerField()
    national_ID = models.CharField(max_length=20)
    email = models.EmailField(max_length=100, blank=True, unique=True)
    password = models.CharField(max_length=20)
    role = models.BooleanField(default=False)