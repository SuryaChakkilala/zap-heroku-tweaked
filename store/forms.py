from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from django import forms

from .models import Order

class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = '__all__'

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User 
        fields = ['username', 'email', 'password1', 'password2']

class UserUpdateForm(ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']