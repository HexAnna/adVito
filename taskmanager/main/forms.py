from .models import Advert, Profile
from django.forms import ModelForm, widgets, TextInput, Textarea, ImageField


class AdvertForm(ModelForm):
    class Meta:
        model = Advert
        fields = ["title", "text"]
        widgets = {
            "title": widgets.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Название'                
            }),
            "text": widgets.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Описание'
            }),
        }
