from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.db import models


class RegisterForm(UserCreationForm):

    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}))

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]

    def __init__(self, *args, **kwargs):
        print("args",kwargs)
        super(RegisterForm, self).__init__(*args, **kwargs)
        for field_name in self.fields:
            self.fields[field_name].widget.attrs['class'] = 'form-control'
            if field_name == 'username':
                self.fields[field_name].widget.attrs['placeholder'] = 'Username'
            elif 'password' in field_name:
                self.fields[field_name].widget.attrs['placeholder'] = 'Password'
            
            # Remove help text
            self.fields[field_name].help_text = None

    def clean(self):
        cleaned_data = super().clean()
        for field in self.fields:
            if field in self.errors:
                self.add_error(field, f"Please enter a valid {field.replace('_', ' ').title()}")
        return cleaned_data

class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}))

    def clean(self):
        cleaned_data = super().clean()
        if self.errors:
            self.add_error(None, "Invalid username or password")
        return cleaned_data
