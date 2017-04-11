from django.shortcuts import render;
from django.http import HttpResponse;
from django.template import loader;
from django.contrib.auth.forms import AuthenticationForm

def index(request):
    template = loader.get_template('home.html');
    return HttpResponse(template.render({}, request));

def login(request):
    form = AuthenticationForm();

    if request.method == 'POST':
        print(request.POST);

    return render(request, 'login.html', { 'form': form });