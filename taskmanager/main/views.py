from django import forms
from django.shortcuts import render, redirect
from .models import Advert, Profile
from .forms import AdvertForm, RegForm
from django.db.models.aggregates import Count
from django.http import HttpResponse




def index(request):
    adverts = Advert.objects.order_by('-id')[:10]
    return render(request, 'main/index.html', {'title': 'Главная страница сайта', 'adverts': adverts})
        
def adverts(request):
    adverts = Advert.objects.order_by('-id')
    return render(request, 'main/adverts.html', {'title': 'Объявления', 'text': 'Описание', 'author': 'Продавец', 'img': 'Картинка', 'likes': 'Нравится', 'date_pub': 'Дата публикации'})

def about(request):
    return render(request, 'main/about.html')

def price(request):
    return render(request, 'main/price.html')


def log_reg(request):
    error = ''
    if request.method == 'POST':
        form = RegForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else: 
            error = "Заполнение некорректное"

    form = RegForm()
    context = {
        'form': form,
        'error': error
    }

    return render(request, 'main/log_reg.html', context)

def add_adv(request):
    error = ''
    if request.method == 'POST':
        form = AdvertForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else: 
            error = "Заполнение некорректное"


    form = AdvertForm()
    context = {
        'form': form,
        'error': error
    }

    return render(request, 'main/add_adv.html', context)


