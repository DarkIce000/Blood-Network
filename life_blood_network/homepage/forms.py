from django import forms
from .models import User, bloodStock

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


class RegistrationForm(forms.ModelForm):
    confirm_password = forms.CharField(max_length=30)
    class Meta:
        model = User
        fields = (
            'first_name',
            'last_name',
            'username',
            'password',
            'confirm_password',
            'email',
            'contact_no',
            'address',
            'city',
            'state',
            'user_type',
            )
        

    
