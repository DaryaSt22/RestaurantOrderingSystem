from django.http import HttpResponse


def index(request):
    return HttpResponse("<h1>Pedro's online restaurant!</h1>")

def menu(request):
    return HttpResponse("<h1>Our menu</h1>")

def orders(request):
    return HttpResponse("<h1>History orders</h1>")