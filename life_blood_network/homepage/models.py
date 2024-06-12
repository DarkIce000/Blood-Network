from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(AbstractUser):
    USER_TYPE =(
        ('provider', 'provider'),
        ('reciever', 'reciever'),
    )
    contact_no = models.CharField(max_length=20, blank=True)
    address = models.CharField(max_length=200, blank=True)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    user_type = models.CharField(max_length=20, choices=USER_TYPE)
    

class bloodStock(models.Model):
    BLOOD_TYPE = (
        ('AP', 'A+'),
        ('AN', 'A-'),
        ('BP', 'B+'),
        ('BN', 'B-'),
        ('ABP', 'AB+'),
        ('ABN', 'AB-'),
        ('OP', 'O+'),
        ('ON', 'O-'),
    )
    blood_bank = models.ForeignKey(User, on_delete=models.CASCADE)
    blood_type = models.CharField(max_length=30, choices=BLOOD_TYPE)
    quantity = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.blood_bank} added {self.quantity} of {self.blood_type}'


class order(models.Model):
    user = models.ManyToManyField(User)
    timestamp = models.DateTimeField(auto_now_add=True)
    blood_type = models.ForeignKey(bloodStock, on_delete=models.PROTECT)
    quantity = models.IntegerField(default=0)
    address = models.CharField(max_length=200)
    prescription = models.ImageField()
    id_proof = models.ImageField()
    id_proof_patient = models.ImageField()

    def __str__(self):
        return f'{self.user} -> {self.blood_type} ordered {self.quantity} of them'
