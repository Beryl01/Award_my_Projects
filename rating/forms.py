from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile, Project, Rating

class Registration(UserCreationForm):
  email = forms.EmailField()
  class Meta:
    model = User
    fields = ['username','email','password1','password2']

class NewProjectForm(forms.ModelForm):
  class Meta:
    model = Project
    exclude = ['poster','postername', 'pub_date']


class NewRatingForm(forms.ModelForm):
  class Meta:
    model = Rating
    exclude = ['project','postername','pub_date']


class NewProfileForm(forms.ModelForm):
  class Meta:
    model = Profile
    exclude = ['user']

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user']  