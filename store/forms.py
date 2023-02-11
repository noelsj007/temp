# model is in store so we can import this to userprofile

from django import forms

from .models import Product, Order

class OrderForm(forms.ModelForm):
    #first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}))
    #last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'}))
    #email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}))
    #mobile = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Mobile'}))
    #address = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Address'}))
    
    class Meta:
        model = Order
        fields = ('first_name', 'last_name', 'email', 'mobile', 'address',)


class ProductForm(forms.ModelForm):
    class ProductForm():
        category = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Category'}))
        title =  forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Product Title'}))
        image =  forms.ImageField(widget= forms.FileInput(attrs={'class': 'form-control', 'placeholder': 'Upload image here', 'label' : 'image'}))
        description = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter description here'}))
        price = forms.IntegerField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter price'}))
        discount_price = forms.IntegerField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter discount price'}))
        quantity = forms.IntegerField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter quantity'}))
        
    class Meta:
        model = Product
        fields = ['category', 'title', 'image', 'description', 'price', 'discount_price', 'quantity']























