from django.urls import path
from . import views
from django.views.generic import TemplateView
from .views import CustomLoginView, login_view
from .views import login
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('register/', views.register, name='register'),
    # path('login/', login, name='login'),
    # path('login/<int:id>/', TemplateView.as_view(template_name="login.html")),
    # path('login/', CustomLoginView.as_view(), name='login'),
    # path('login/', login_view, name='login'),
    #path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('login/', views.custom_login, name='login')
]