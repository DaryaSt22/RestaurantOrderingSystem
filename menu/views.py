from django.shortcuts import render
from .models import Dish


def menu_view(request):
    dishes = Dish.objects.filter(available=True)
    return render(request, 'menu/menu.html', {'dishes': 'dishes'})
