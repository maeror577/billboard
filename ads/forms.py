from django.forms import ModelForm
from .models import Ad


class AdForm(ModelForm):
    class Meta:
        model = Ad
        fields = ['title', 'category', 'content']
