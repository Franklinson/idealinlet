from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from .models import *


class AuthorForm(ModelForm):
	class Meta:
		model = Author
		fields = '__all__'
		exclude = ['user']


class AbstractForm(ModelForm):
    class Meta:
        model = Abstract
        fields = '__all__'


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']