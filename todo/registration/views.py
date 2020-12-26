from django.shortcuts import render, reverse, redirect
from registration.models import CustomsUserCreationForm, LoginForm
from django.contrib.auth import login, authenticate


def registration_view(request):
    form = CustomsUserCreationForm
    if request.method == 'POST':
        form = CustomsUserCreationForm(data=request.POST)
        if form.is_valid():
            success_url = reverse('registration:login')
            form.save()
            return redirect(success_url)
    contex = {
        'form': form
    }
    return render(request, 'registration.html', contex)


def login_view(request):
    form = LoginForm
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('login')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user and user.is_active:
                login(request, user)
                success_url = reverse('main:main')
                return redirect(success_url)
    contex = {
        'form': form
    }
    return render(request, 'login.html', contex)
