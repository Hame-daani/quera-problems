from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login as dj_login, logout as dj_logout
from django.shortcuts import redirect, render
from django.urls import reverse
from account.forms import *


def home(request):
    # TODO
    if request.method == 'GET':
        try:
            team = request.user.team.name
        except:
            team = None
        return render(request, 'home.html', {'team': team})


def signup(request):
    if request.method == 'GET':
        form = SignUpForm()
        return render(request, 'signup.html', {'form': form})
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            dj_login(request, user)
            return redirect('team')
        else:
            return render(request, 'signup.html', {'form': form})


def login_account(request):
    if request.method == 'GET':
        form = LoginForm()
        return render(request, 'login.html', {'form': form})
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form .cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user:
                dj_login(request, user)
                return redirect('home')
        # TODO
        return render(request, 'login.html', {'form': form})


def logout_account(request):
    if request.method == 'GET':
        dj_logout(request)
        return redirect('login')


@login_required(login_url='login')
def joinoradd_team(request):
    # TODO
    if request.method == 'GET':
        if request.user.team:
            return redirect('home')
        else:
            form = TeamForm()
            return render(request, 'team.html', {'form': form})
    if request.method == 'POST':
        form = TeamForm(request.POST)
        if form.is_valid():
            team, created = Team.objects.get_or_create(
                name=form.cleaned_data['name'])
            if created:
                team.jitsi_url_path = f"http://meet.jit.si/{team.name}"
                team.save()
            user = request.user
            user.team = team
            user.save()
        return redirect('home')


def exit_team(request):
    # TODO
    if request.method == 'GET':
        user = request.user
        if user.team:
            user.team = None
            user.save()
        return redirect('home')
