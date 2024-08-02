from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.db import models
from core.models import Khsetra,Mandir,Mandal,Haribhakt


class RegisterForm(UserCreationForm):

    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}))

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]

    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)
        for field_name in self.fields:
            self.fields[field_name].widget.attrs['class'] = 'form-control my-2'
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
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control my-2', 'placeholder': 'Username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}))

    def clean(self):
        cleaned_data = super().clean()
        if self.errors:
            self.add_error(None, "Invalid username or password")
        return cleaned_data

class MandirForm(forms.ModelForm):
    class Meta:
        model = Mandir
        fields = '__all__'

# class KhsetraForm(forms.ModelForm):
#     class Meta:
#         model = Khsetra
#         fields = '__all__'

# class MandalForm(forms.ModelForm):
#     class Meta:
#         model = Mandal
#         fields = '__all__'

# class HaribhaktForm(forms.ModelForm):
#     class Meta:
#         model = Haribhakt
#         fields = '__all__'
