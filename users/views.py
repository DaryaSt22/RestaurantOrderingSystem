from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView

from django.contrib.auth.decorators import login_required

from .forms import LoginUserForm

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('menu')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})


def login(request):
    if request.method == 'POST':
        form = LoginUserForm(request.POST)
        if form.is_valid():
            user = authenticate(
                request,
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password']
            )
            if user is not None:
                login(request, user)
                return redirect('menu')
            else:
                form.add_error(None, 'Неверный логин или пароль')
        else:
            form = LoginUserForm()
        return render(request, 'login.html', {'form': form})
            #cd = form.cleaned_data
            #user = authenticate(request, username=cd['username'], password=cd['password'])
    #     if user and user.is_active:
    #         login(request, user)
    #         return HttpResponseRedirect(reverse(''))
    # else:
    #     form = LoginUserForm()
    #     return render(request, 'users/login.html', {'form': 'form'})

def logout_user(request):
    return HttpResponse("logout")


class CustomLoginView(LoginView):
    template_name = 'login.html'
    authentication_form = AuthenticationForm
    redirect_authenticated_user = True


@login_required
def login_view(request):
    return render(request, 'login.html')


def custom_login(request):
    form = LoginUserForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            user = authenticate(
                request,
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password']
            )
            if user is not None:
                login(request, user)
                return redirect('home')  # замените на нужный URL
            else:
                form.add_error(None, "Неверные данные")


    return render(request, 'login.html', {'form': form})