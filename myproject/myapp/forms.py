from django import forms 
from django.forms.fields import EmailField 
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


class LoginForm(forms.Form): 
   Username = forms.CharField(max_length=100) 
   Password = forms.CharField(max_length=100)
   
class RegForm(forms.Form):
   Username = forms.CharField(max_length=100) 
   Email = forms.EmailField(required=True)
   Password = forms.CharField(max_length=100)

class AddressForm(forms.Form):
   Name = forms.CharField(max_length=200)
   Email = forms.EmailField(required=True)
   Mobile= forms.IntegerField(required=True)
   Address = forms.CharField(max_length=500)