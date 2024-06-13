from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(AbstractUser):
    USER_TYPE =(
        ('provider', 'provider'),
        ('reciever', 'reciever'),
    )
    profile_img = models.ImageField(upload_to="profile_img/", blank=True)
    contact_no = models.CharField(max_length=200, blank=True)
    address = models.CharField(max_length=200, blank=True)
    city = models.CharField(max_length=100, blank=True)
    state = models.CharField(max_length=100, blank=True)
    user_type = models.CharField(max_length=20, choices=USER_TYPE)
    

class bloodStock(models.Model):
    BLOOD_TYPE = (
        ('A+', 'A+'),
        ('A-', 'A-'),
        ('B+', 'B+'),
        ('B-', 'B-'),
        ('AB+', 'AB+'),
        ('AB-', 'AB-'),
        ('O+', 'O+'),
        ('O-', 'O-'),
    )


    blood_bank = models.ForeignKey(User, on_delete=models.CASCADE)
    blood_type = models.CharField(max_length=30, choices=BLOOD_TYPE)
    quantity = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.blood_bank} added {self.quantity} of {self.blood_type}'


class order(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    timestamp = models.DateTimeField(auto_now_add=True)
    blood_type = models.ForeignKey(bloodStock, on_delete=models.PROTECT)
    quantity = models.IntegerField(default=0)
    address = models.CharField(max_length=200)
    prescription_img = models.ImageField(upload_to="prescription_img/")
    id_proof = models.ImageField(upload_to="id_proof/")
    id_proof_patient = models.ImageField(upload_to="id_proof_patient/")

    def __str__(self):
        return f'{self.user} -> {self.blood_type} ordered {self.quantity} of them'
