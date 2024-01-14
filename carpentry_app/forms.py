# carpentry_app/forms.py
from django import forms
from .models import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'phone', 'address', 'description']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter your email'}),
            'phone': forms.TextInput(
                attrs={'class': 'form-control', 'id': 'inputPhone', 'placeholder': 'Enter your phone number'}),
            'address': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your address'}),
            'description': forms.Textarea(
                attrs={'class': 'form-control', 'id': 'inputDescription', 'placeholder': 'Enter your description'}),
        }
