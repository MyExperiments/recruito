from django.shortcuts import render;
from django.contrib.auth.forms import AuthenticationForm

def login(request):
    form = AuthenticationForm();

    if request.method == 'POST':
        print(request.POST);

    return render(request, 'login.html', { 'form': form });