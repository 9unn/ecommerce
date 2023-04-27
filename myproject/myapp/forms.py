from django import forms 
from myapp.models import *
from django.forms.fields import EmailField 
from django.contrib.auth.models import User
from crispy_forms.helper import FormHelper
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


class LoginForm(forms.Form): 
   username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Username'}))
   password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))

   class Meta:
        model = User
        fields = ('username', 'password')

   def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_show_labels = False
   
# class RegForm(forms.Form):
#    Username = forms.CharField(max_length=100) 
#    Email = forms.EmailField(required=True)
#    Password = forms.CharField(max_length=100)

class RegForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'First name'}))
    surname = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Last name'}))
    phone = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Phone number'}))
    address = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Address'}))
    email = forms.CharField(widget=forms.EmailInput(attrs={'placeholder': 'Email'}))
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))

    class Meta:
        model = User
        fields = [('username', 'email', 'first_name', 'last_name', 'password1', 'password2')]

    def __init__(self, *args, **kwargs):
        super(RegForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_show_labels = False

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError(
                "Customer with this useername already exists")
        

class AddressForm(forms.Form):
   Name = forms.CharField(max_length=200)
   Email = forms.EmailField(required=True)
   Mobile= forms.IntegerField(required=True)
   Address = forms.CharField(max_length=500)