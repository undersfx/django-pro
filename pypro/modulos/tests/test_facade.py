import pytest
from pypro.modulos import facade
from model_bakery import baker
from pypro.modulos.models import Modulo


@pytest.fixture()
def modulos(db):
    return [baker.make(Modulo, titulo=s) for s in ['A', 'B', 'C']]


def test_lista_modulos_ordenados(modulos):
    assert list(sorted(modulos, key=lambda modulo: modulo.order)) == facade.lista_modulos_ordenados()
