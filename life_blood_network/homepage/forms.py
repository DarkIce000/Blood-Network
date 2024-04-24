from django import forms
from .models import User, bloodStock
from django.contrib.auth.forms import UserCreationForm

class ProfilePageForm(forms.ModelForm):
    class Meta:
        model = User
        fields = (
            'first_name',
            'last_name',
            'username',
            'email',
            'address',
            'city',
            'state',
            'contact_no',
            'user_type',
        )


class BloodStockForm(forms.ModelForm):
    class Meta:
        model = bloodStock
        fields = (
            'blood_type', 
            'quantity'
        )


class RegistrationForm(UserCreationForm):
    confirm_password = forms.CharField(max_length=30)
    class Meta:
        model = User
        fields = (
            'first_name',
            'last_name',
            'username',
            'password1',
            'password2',
            'email',
            'contact_no',
            'address',
            'city',
            'state',
            'user_type',
            )
        

    
