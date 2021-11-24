from django.urls import path
from . import views
from django.contrib import admin

urlpatterns = [
    path('', views.index, name='home'),
    path('log_reg', views.log_reg, name='log_reg'),
    path('about-us', views.about, name='about'),
    path('add_adv', views.add_adv, name='add_adv'),
    path('sellers', views.sellers, name='sellers'),
    path('adverts', views.adverts, name='adverts'),
    path('price', views.price, name='price'),
]