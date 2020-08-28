from django import forms
from .models import List
from django.contrib.auth.models import User
from datetime import datetime

class list_input(forms.ModelForm):

        class Meta:
            model = List
            exclude = ('datetimemade','user',)

class loginform(forms.Form):
       username = forms.CharField(max_length=30)
       password = forms.CharField(widget=forms.PasswordInput())



