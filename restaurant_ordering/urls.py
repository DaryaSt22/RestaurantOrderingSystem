"""
URL configuration for restaurant_ordering project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from restaurant_ordering import views
from django.views.generic import TemplateView

app_name = 'restaurant_ordering'

urlpatterns = [
    #re_path(r'^menu/', views.menu, name='menu'),
    #re_path(r'^orders/', views.orders, name='orders'),
    re_path(r'^users/', include('users.urls')),
    re_path(r'^accounts/', include('django.contrib.auth.urls')),
    # path('', views.index, name="Pedro's online restaurant"),
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name="index.html")),
    path('login_user/<int:id>/', TemplateView.as_view(template_name="login.html")),
    re_path(r'^login/', views.login, name='login'),
    path('register/<int:id>/', TemplateView.as_view(template_name="users/register.html")),
    re_path(r'^menu/', TemplateView.as_view(template_name="menu.html")),
    re_path(r'^orders/', TemplateView.as_view(template_name="orders.html")),
]
