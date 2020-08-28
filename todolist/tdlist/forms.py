from django import forms
from .models import List
from django.contrib.auth.models import User
from datetime import datetime

class list_input(forms.ModelForm):

        class Meta:
            model = List
            exclude = ('datetimemade','user',)

class loginform(forms.ModelForm):
       class Meta:
           model = User
           fields = ['username','password']


