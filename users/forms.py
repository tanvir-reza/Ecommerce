from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile
from django.db.models import Q


class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['name', 'phone', 'Shipping_address']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
            'Shipping_address': forms.TextInput(attrs={'class': 'form-control'}),
        }