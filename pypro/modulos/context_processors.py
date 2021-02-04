from pypro.modulos import facade


def listar_modulos(request):
    return {'MODULOS': facade.lista_modulos_ordenados()}
