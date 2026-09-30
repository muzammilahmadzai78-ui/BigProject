from django import forms
from .models import Product, Profile
from django.contrib.auth.models import User

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['image', 'name', 'sku', 'price', 'quantity', 'supplier', 'category']
        labels = {
            'product_id': 'Product ID',
            'name': 'Name',
            'sku': 'SKU',
            'price': 'Price',
            'quantity': 'Quantity',
            'supplier': 'Supplier',
            'category': 'Category',
        }

        widgets = {
            'product_id': forms.NumberInput(attrs={'placeholder': 'e.g. 1',  'class': 'form-control'}),
            'name': forms.TextInput(attrs={'placeholder': 'e.g. Shirt',  'class': 'form-control'}),
            'sku': forms.TextInput(attrs={'placeholder': 'e.g V234',  'class': 'form-control'}),
            'price': forms.NumberInput(attrs={'placeholder': 'e.g. 19.99',  'class': 'form-control'}),
            'quantity': forms.NumberInput(attrs={'placeholder': 'e.g. 10',  'class': 'form-control'}),
            'supplier': forms.TextInput(attrs={'placeholder': 'e.g. ABC Corps',  'class': 'form-control'}),
            'category': forms.TextInput(attrs={'placeholder': 'e.g. Computer',  'class': 'form-control'}),
            'image': forms.FileInput(attrs={'class': 'image'}),
        }



class RegisterForm(forms.ModelForm):
    username = forms.CharField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)
    email = forms.EmailField()
    class Meta:
        model = User
        fields = [
            'username', 'password', 'confirm_password', 'first_name', 'last_name', 'email'
        ]


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['phone_number', 'image']
        