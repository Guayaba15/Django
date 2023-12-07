# myapp/forms.py
from django import forms
from .models import UserProfile


class RegistrationForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['username', 'email', 'password']
        widgets = {'password': forms.PasswordInput()}

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())
    next_url = forms.CharField(required=False, widget=forms.HiddenInput())