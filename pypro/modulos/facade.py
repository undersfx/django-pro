from typing import List
from pypro.modulos.models import Modulo


def lista_modulos_ordenados() -> List[Modulo]:
    """
    Lista módulos ordenados por título
    :return: List[Modulo]
    """
    queryset = Modulo.objects.order_by('order').all()
    return list(queryset)


def encontrar_modulo(slug: str) -> Modulo:
    return Modulo.objects.get(slug=slug)


def encontrar_aulas_por_modulo_ordenadas(modulo: Modulo):
    return list(modulo.aula_set.order_by('order').all())
