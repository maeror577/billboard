from django import forms
from django.forms import ModelForm
from .models import Ad, Offer


class AdForm(ModelForm):
    class Meta:
        model = Ad
        fields = ['title', 'category', 'content']


class OfferForm(ModelForm):
    class Meta:
        model = Offer
        fields = ['user', 'ad', 'text']
        widgets = {
            'text': forms.Textarea(attrs={'placeholder': 'Enter your offer'})
        }
