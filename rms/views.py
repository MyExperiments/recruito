from django.shortcuts import render;
from django.http import HttpResponse;
from django.template import loader;
from .forms import LoginForm

def index(request):
    template = loader.get_template('home.html');
    return HttpResponse(template.render({}, request));

def login(request):
    template = loader.get_template('login.html');
    form = LoginForm;
    return HttpResponse(template.render({'form': form}, request));