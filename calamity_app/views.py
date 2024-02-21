# calamity_app/views.py
from .models import Calamity, MitigationStrategy
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout

def landing_page(request):
    return render(request, 'calamity_app/landing_page.html')

def about_us(request):
    return render(request, 'calamity_app/about_us.html')

def login(request):
    # Your login logic goes here
    return render(request, 'calamity_app/login.html')

def calamity_list(request):
    calamities = Calamity.objects.all()
    return render(request, 'calamity_app/calamity_list.html', {'calamities': calamities})

def calamity_detail(request, calamity_id):
    calamity = Calamity.objects.get(id=calamity_id)
    mitigation_strategies = MitigationStrategy.objects.filter(calamity=calamity)
    return render(request, 'calamity_app/calamity_detail.html', {'calamity': calamity, 'mitigation_strategies': mitigation_strategies})

def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('calamity_list')
    else:
        form = UserCreationForm()
    return render(request, 'calamity_app/signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('calamity_list')
    else:
        form = AuthenticationForm()
    return render(request, 'calamity_app/login.html', {'form': form})

def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('calamity_list')