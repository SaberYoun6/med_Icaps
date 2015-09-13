from django.shortcuts import render
from django.contrib.auth import authenticate, login
from datetime import date

# Create your views here.

def calendar(request):
    return render(request, 'calendar.html', {})

def index(request):
    return render(request, 'index.html', {})

from django.http import *
from django.shortcuts import render_to_response,redirect
from django.template import RequestContext
from django.contrib.auth import authenticate, login, logout

def login_user(request):
    logout(request)

    today = date.today()
    year = today.year
    month = today.month


    username = password = ''
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                string = "/calendar"+str(year)+"/"+str(month)+str("/")
                return HttpResponseRedirect(string)
    return render_to_response('login.html', context_instance=RequestContext(request))
