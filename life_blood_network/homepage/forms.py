from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm



BOOTSTRAP_CLASS = { 
    'class': 'form-control my-2',
}
# Type of Input 
file_upload = forms.FileInput(attrs=BOOTSTRAP_CLASS)

STYLE_2 ={
            'profile_img': file_upload,
            'prescription_img': file_upload,
            'id_proof': file_upload, 
            'id_proof_patient': file_upload,
            'address': forms.Textarea(attrs=BOOTSTRAP_CLASS),
            'first_name': forms.TextInput(attrs=BOOTSTRAP_CLASS),
            'last_name': forms.TextInput(attrs=BOOTSTRAP_CLASS),
            'username': forms.TextInput(attrs=BOOTSTRAP_CLASS),
            'email': forms.TextInput(attrs=BOOTSTRAP_CLASS),
            'password1': forms.PasswordInput(attrs=BOOTSTRAP_CLASS),
            'password2': forms.PasswordInput(attrs=BOOTSTRAP_CLASS),
            'contact_no': forms.TextInput(attrs=BOOTSTRAP_CLASS),
            'city': forms.TextInput(attrs=BOOTSTRAP_CLASS),
            'state': forms.TextInput(attrs=BOOTSTRAP_CLASS),
            'user_type': forms.Select(choices=User.USER_TYPE, attrs=BOOTSTRAP_CLASS),
            'blood_type': forms.Select(choices=bloodStock.BLOOD_TYPE, attrs=BOOTSTRAP_CLASS), 
            'quantity': forms.NumberInput(attrs=BOOTSTRAP_CLASS)
        }   


class ProfilePageForm(forms.ModelForm):
    class Meta:
        model = User
        fields = (
            'first_name',
            'last_name',
            'profile_img',
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
        widgets = STYLE_2


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
            'profile_img',
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

    
class orderForm(forms.ModelForm):
    class Meta:
        model = order 
        fields = (
            'quantity', 
            'address',
            'prescription_img',
            'id_proof', 
            'id_proof_patient',
        )
        # mod_STYLE_2 = STYLE_2
        # mod_STYLE_2['quantity'] = forms.NumberInput(attrs={
        #     "class":"form-control my-2",
        #     "min":1, 
        #     "max":"{{blood_details.quantity}}",
        # })

        widgets = STYLE_2