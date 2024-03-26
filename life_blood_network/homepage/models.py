from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(AbstractUser, models.Model):
    provider = models.BooleanField(default=False)  
    reciever = models.BooleanField(default=False)  

class bloodProvider(models.Model):
    provider = models.OneToOneField(User, on_delete=models.CASCADE) 
    address = models.CharField(max_length=100)
    contact_no = models.IntegerField()

class bloodReciever(models.Model):
    reciever = models.OneToOneField(User, on_delete=models.CASCADE) 
    profile_picture = models.ImageField(upload_to="images/")
    address = models.CharField(max_length=100)
    contact_no = models.IntegerField()

class bloodGroup(models.Model):
    APositive = models.IntegerField()
    ANegative = models.IntegerField()
    ABPositive = models.IntegerField()
    ABNegative = models.IntegerField()
    OHPositive = models.IntegerField()
    OHNegative = models.IntegerField()
    OPositive = models.IntegerField()
    ONegative = models.IntegerField() 
