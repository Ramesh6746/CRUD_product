from django import forms
from django.forms import fields, widgets
from .models import User
from django.core import validators

class Studentregi(forms.ModelForm):
    class Meta:
        model = User
        fields = ['name','email','password']
        widgets = {
            'name':forms.TextInput(),
            'email':forms.EmailInput(),
            'password':forms.TextInput(),
        }