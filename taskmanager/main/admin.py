from django.contrib import admin
from django.forms import ModelChoiceField
from .models import *
from django import forms
from .models import Advert, Cart, CartProduct, Category, Customer, Notebook, Smartfone
from PIL import Image


class NotebookAdmin(admin.ModelAdmin):

    MIN_RESOLUTION = (400, 400)

    def __init__(self, *args, **kwargs):
        super().__init__( *args, **kwargs)
        self.fields['image'].help_text = 'Мининимальное разрешение для загрузки изображения {}x{}'.format(
            *self.MIN_RESOLUTION)

    def clean_image(self):
        image = self.cleaned_data['image']
        img = Image.open(image)
        min_heigh, min_widh = self.MIN_RESOLUTION
        if img.height < min_heigh or img.width < min_widh:
            raise ValueError('Загруженное изображение слишком маленькое')
        return image
    

class NotebookAdmin(admin.ModelAdmin):

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'category':
            return ModelChoiceField(Category.objects.filter(slug='notebooks'))
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


class SmartfoneAdmin(admin.ModelAdmin):

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'category':
            return ModelChoiceField(Category.objects.filter(slug='smartfone'))
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

admin.site.register(Category)
admin.site.register(CartProduct)
admin.site.register(Notebook, NotebookAdmin)
admin.site.register(Smartfone, SmartfoneAdmin)
admin.site.register(Cart)
admin.site.register(Customer)
admin.site.register(Advert)
