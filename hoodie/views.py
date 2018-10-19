from django.shortcuts import render
from django.contrib.auth.decorators import login_required


# Create your views here.


@login_required(login_url='/accounts/login/')
def home(request):
    return render(request, 'index.html')


@login_required(login_url='/accounts/login/')
def loader(request):
    return render (request, 'loader.html')