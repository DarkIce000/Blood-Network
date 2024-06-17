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
    blood_details = models.ForeignKey(bloodStock, on_delete=models.PROTECT)
    quantity = models.IntegerField(default=1)
    address = models.CharField(max_length=200)
    prescription_img = models.ImageField(upload_to="prescription_img/")
    id_proof = models.ImageField(upload_to="id_proof/")
    id_proof_patient = models.ImageField(upload_to="id_proof_patient/")
    approve_status = models.BooleanField(default=False)
    cancel_status = models.BooleanField(default=False)
    rejected_status = models.BooleanField(default=False)

    def serialize(self):
        return {
            "id": self.id,
            "user": self.user.first_name,
            "user_address": self.user.address,
            "blood_bank": self.blood_details.blood_bank.first_name,
            "blood_bank_address": self.blood_details.blood_bank.address,
            "delivery_address": self.address, 
            "blood_type": self.blood_details.blood_type,
            "quantity": self.quantity,
            "prescription_img": self.prescription_img.url,
            "user_id_proof": self.id_proof.url,
            "id_proof_patient": self.id_proof_patient.url, 
            "approve_status": self.approve_status,
            "cancel_status": self.cancel_status,
            "rejected_status": self.rejected_status,
            "timestamp": self.timestamp
        }
                                      