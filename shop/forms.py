from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms


class RegisterForm(UserCreationForm):
    
    first_name = forms.CharField(max_length=30,label='', required=True,widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}))
    last_name = forms.CharField(max_length=30, label='',required=True,widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'}))
    email = forms.EmailField(max_length=50,label='',required=True,widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': ' Email'}))
    username= forms.CharField(max_length=30, label='',required=True,widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'username', 'name': 'username', 'type': 'text'}))
    password1 = forms.CharField(max_length=30, label='',required=True,widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'password', 'name': 'password', 'type': 'password'}))
    password2 = forms.CharField(max_length=30, label='',required=True,widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'password again', 'name': 'password', 'type': 'password'}))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')
    