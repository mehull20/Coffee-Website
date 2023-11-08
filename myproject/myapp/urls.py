from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('hi/', views.hello, name = "hello_world"), #views.hello is defined in views file. and my path will be myapp/hi and after that it should import hello function, therefore importing using views.py
    path('my_view', views.my_view, name="index"),
    path('login', views.login, name='login'),
    path('hot', views.hotcoffee, name='hot'),
    path('frappes', views.frappes, name='frappes'),
    path('iced', views.iced, name='iced')
]
