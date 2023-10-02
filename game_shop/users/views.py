from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout

from .forms import RegisterForm, LoginForm


def signupuser(request):
    if request.user.is_authenticated:
        return redirect(to='shop_app:main')

    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(to='shop_app:main')
        else:
            return render(request, 'users/signup.html', context={"form": form})

    return render(request, 'users/signup.html', context={"form": RegisterForm()})


def loginuser(request):
    if request.user.is_authenticated:
        return redirect(to='noteapp:main')

    if request.method == 'POST':
        user = authenticate(username=request.POST['username'], password=request.POST['password'])
        if user is None:
            messages.error(request, 'Username or password didn\'t match')
            return redirect(to='users:login')

        login(request, user)
        return redirect(to='noteapp:main')

    return render(request, 'users/login.html', context={"form": LoginForm()})
