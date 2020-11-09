from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from App_Login.models import UserProfile

class CreateNewUser(UserCreationForm):
    email = forms.EmailField(label="",widget=forms.TextInput(attrs={'placeholder':'Email'}))
    username = forms.CharField(required=True,label="",widget=forms.TextInput(attrs={'placeholder':'Username'}))
    password1= forms.CharField(required=True ,label="", widget=forms.PasswordInput(attrs={'placeholder':'password'}))
    password2=forms.CharField(required=True,label="",widget=forms.PasswordInput(attrs={'placeholder':'Repeat password'}))
    class Meta:
        model = User
        fields = ('username','email','password1','password2')


class EditProfile(forms.ModelForm):
    dob = forms.CharField(widget=forms.TextInput(attrs={'type':'date'}))
    class Meta:
        model = UserProfile()
        exclude = ('user',)
