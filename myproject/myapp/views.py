from django.shortcuts import render, redirect
from django.http import HttpResponse
from.forms import loginForm

# Create your views here.
def hello(request):
    return HttpResponse("<marquee><h1>Hello World!</h1></marquee>")
def my_view(request):
    context = {"author":"Mehul Goyal"}
    return render(request, "index.html") #no template
    return render(request, "my_view.html", context)

def hotcoffee(request):
    return render(request, "hot.html")

def frappes(request):
    return render(request, "frappes.html")

def iced(request):
    return render(request, "iced.html")


def login(request):
    return render(request, 'login.html') 