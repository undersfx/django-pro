import pytest
from pypro.django_assertions import assert_contains
from django.urls import reverse
from model_bakery import baker
from pypro.modulos.models import Modulo


@pytest.fixture()
def modulo(db):
    return baker.make(Modulo)


@pytest.fixture()
def resp(client, modulo: Modulo):
    resp = client.get(reverse('modulos:detalhe', kwargs={'slug': modulo.slug}))
    return resp


def test_titulo(resp, modulo: Modulo):
    assert_contains(resp, modulo.titulo)


def test_publico(resp, modulo: Modulo):
    assert_contains(resp, modulo.publico)


def test_descricao(resp, modulo: Modulo):
    assert_contains(resp, modulo.descricao)
