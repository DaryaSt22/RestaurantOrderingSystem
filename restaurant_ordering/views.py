from django.http import HttpResponse
from django.shortcuts import render
from users.forms import LoginUserForm


def index(request):
    return HttpResponse("<h1>Pedro's online restaurant!</h1>")

def menu(request):
    return HttpResponse("<h1>Our menu</h1>")

def orders(request):
    return HttpResponse("<h1>History orders</h1>")


def login(request):
    form = LoginUserForm()
    return render(request, 'registration/login.html', {'form': 'form'})