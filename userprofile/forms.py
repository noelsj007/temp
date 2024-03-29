from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.forms import ModelForm

from .models import CustomUser
from django.db import models
from store.models import Vendor


class UserAdminCreationForm(UserCreationForm):
    CHOICES = (
        ('yes', 'Yes'),
        ('no', 'No'),
    )

    """
    A Custom form for creating new users.
    """
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}))

    last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'}))

    mobile = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Mobile'}))

    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}))
    
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}))

    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirm Password'}))

    is_vendor = forms.ChoiceField(widget=forms.RadioSelect(attrs={'name': 'is_vendor'}),choices=CHOICES, initial='no')
    
    #vendor_name = forms.ModelChoiceField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Vendor name'}),  queryset = forms.CharField(max_length=255, initial=Vendor.objects.all()[0].vendor_name))

    #vendor_address = forms.ModelChoiceField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Vendor address'}),  queryset = forms.CharField(max_length=255, initial=Vendor.objects.all()[0].vendor_address))

    #vendor_name = models.ForeignKey(Vendor, related_name='vendors', on_delete=models.CASCADE)

    #vendor_address = models.ForeignKey(Vendor, related_name='vendors', on_delete=models.CASCADE)

    class Meta:    
        model = get_user_model()
        fields = ['first_name', 'last_name', 'mobile', 'email', 'password1', 'password2', 'is_vendor']



class BecomeVendorForm(forms.ModelForm):
    CHOICES = (
        ('yes', 'Yes'),
        ('no', 'No'),
    )
    vednor_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Vendor or business Name', 'label' : 'vendor_name'}))
    vednor_address = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Vendor address', 'label' : 'vendor_address'}))
    vendor_image = forms.ImageField(widget= forms.FileInput(attrs={'class': 'form-control', 'placeholder': 'Upload image here', 'label' : 'vendor_image'}))

    class Meta:
        model = Vendor
        fields = ('vendor_name', 'vendor_address', 'vendor_image')
    model = CustomUser
    is_vendor = forms.ChoiceField(widget=forms.RadioSelect(attrs={'name': 'is_vendor'}),choices=CHOICES, initial='yes')