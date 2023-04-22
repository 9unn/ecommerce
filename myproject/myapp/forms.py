from django import forms 
from django.forms.fields import EmailField 
from django.forms.widgets import Textarea 

class LoginForm(forms.Form): 
   Username = forms.CharField(max_length=100) 
   Password = forms.CharField(max_length=100)
   
class RegForm(forms.Form):
   Username = forms.CharField(max_length=100) 
   Email = forms.EmailField()
   Password = forms.CharField(max_length=100)

class AddressForm(forms.Form):
   Name = forms.CharField(max_length=200)
   Email = forms.EmailField()
   Mobile= forms.IntegerField()
   Address = forms.CharField(max_length=500)