from django.shortcuts import render

# Create your views here.

def calendar(request):
    return render(request, 'calendar.html', {})

def index(request):
    return render(request, 'index.html', {})

def login(request):
    return render(request, 'login.html', {})

