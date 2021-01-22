from django.shortcuts import render


# Create your views here.
from django.urls import reverse


def home(request):
    contexto = {
        'aperitivos': reverse('aperitivos:index')
    }
    return render(request, 'base/home.html', context={'contexto': contexto})
