from django import forms
from .models import Profile,Blogpost
from django.contrib.auth.forms import  UserCreationForm
from django.contrib.auth.models import  User

class profileform(forms.ModelForm):

     class Meta:
         model = Profile
         fields = '__all__'

class loginform(forms.Form):
    username = forms.CharField(max_length=30)
    password = forms.CharField(max_length=20)


class createuserform(UserCreationForm):
    email = forms.EmailField(max_length=20 ,help_text="required email")
    dob = forms.CharField(max_length=20)
    bio = forms.CharField(widget=forms.Textarea)
    class Meta:
        model = User
        fields =['username','password1','password2','email','dob','bio']



class blogform(forms.ModelForm):

    class Meta:
        model = Blogpost
        fields = ['text','heading','subheading','category']
