from django.shortcuts import render

from pypro.modulos import facade


def indice(request):
    return render(request, 'modulos/indice.html')


def detalhe(request, slug):
    modulo = facade.encontrar_modulo(slug)
    aulas = facade.encontrar_aulas_por_modulo_ordenadas(modulo)
    return render(request, 'modulos/modulo_detalhe.html', context={'modulo': modulo, 'aulas': aulas})


def aula(request, slug):
    aula = facade.encontrar_aula(slug)
    return render(request, 'modulos/aula_detalhe.html', context={'aula': aula})
