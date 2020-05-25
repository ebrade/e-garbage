from django.shortcuts import render


# Create your views here.


def home(request):
    return render(request, 'egarbage/home.html')


def about(request):
    return render(request, 'egarbage/about.html')


def history(request):
    return render(request, 'egarbage/history.html')


def register(request):
    return render(request, 'egarbage/register.html')
