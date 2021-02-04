from typing import List
from pypro.modulos.models import Modulo


def lista_modulos_ordenados() -> List[Modulo]:
    """
    Lista módulos ordenados por título
    :return: List[Modulo]
    """

    return list(Modulo.objects.order_by('titulo').all())