from django import forms
from .models import User, bloodStock, order
from django.contrib.auth.forms import UserCreationForm



STYLE = { 
    'class': 'form-control my-2',
}


STYLE_2 ={
            'address': forms.Textarea(attrs=STYLE),
            'first_name': forms.TextInput(attrs=STYLE),
            'last_name': forms.TextInput(attrs=STYLE),
            'username': forms.TextInput(attrs=STYLE),
            'email': forms.TextInput(attrs=STYLE),
            'password1': forms.PasswordInput(attrs=STYLE),
            'password2': forms.PasswordInput(attrs=STYLE),
            'contact_no': forms.TextInput(attrs=STYLE),
            'city': forms.TextInput(attrs=STYLE),
            'state': forms.TextInput(attrs=STYLE),
            'user_type': forms.Select(choices=User.USER_TYPE, attrs=STYLE)
        }   


class ProfilePageForm(forms.ModelForm):
    class Meta:
        model = User
        fields = (
            'first_name',
            'last_name',
            'email',
            'address',
            'city',
            'state',
            'contact_no',
            'user_type',
        )

        widgets = STYLE_2


class BloodStockForm(forms.ModelForm):
    class Meta:
        model = bloodStock
        fields = (
            'blood_type', 
            'quantity'
        )


class RegistrationForm(UserCreationForm):
    password1 = forms.CharField(
        label = 'Password',
        widget = forms.PasswordInput(attrs={
            'class':'form-control',
            'type':'password',
            'placeholder':'More than or equal to 8 characters. at least one symbol, one uppercase, one number'
        })

    )
    
    password2 = forms.CharField(
        label = 'Confirm Password',
        widget = forms.PasswordInput(attrs={
            'class':'form-control',
            'type':'password',
            'placeholder':'Confirm Password'
        })
    )

    class Meta(UserCreationForm.Meta):
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

        widgets = STYLE_2

    
class order(forms.ModelForm):
    model = order
    fields = (
        'blood_type'
        'quantity'
        'address'
        'prescription'
        'id_proof'
        'id_proof_patient'
    )

    
