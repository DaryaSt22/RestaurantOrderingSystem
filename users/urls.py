from django.urls import path
from . import views
from django.views.generic import TemplateView

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/<int:id>/', TemplateView.as_view(template_name="login.html"))
]