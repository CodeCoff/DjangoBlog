from django import forms
from django.contrib.auth.models import User
# we will use UserCreationForm to create a new user. This is a very common 
# thing for many websites which is why django provides it to us
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

#we need this class to add 'email' field to our registration form
class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        #model that will be affected
        model = User
        #fields that are going to be shown in our form
        fields = ['username', 'email', 'password1', 'password2']

#this will let the user to update their profile
class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        #model that will be affected i.e. User
        model = User
        fields = ['username', 'email']

#this will let the user to update their profile
class ProfileUpdateForm(forms.ModelForm):

    class Meta:
        #model that will be affected i.e. Profile 
        model = Profile
        fields = ['image']
