from django.shortcuts import render;
from django.http import HttpResponse;
from django.template import loader;

def index(request):
    template = loader.get_template('home.html');
    return HttpResponse(template.render({}, request));

def login(request):
    template = loader.get_template('login.html');
    return HttpResponse(template.render({}, request));