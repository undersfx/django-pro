import pytest
from django.urls import reverse
from model_bakery import baker


@pytest.fixture()
def resp(client, db):
    resp = client.get(reverse('login'))
    return resp


def test_status_code(resp):
    assert resp.status_code == 200


@pytest.fixture()
def usuario(db, django_user_model):
    _usuario = baker.make(django_user_model)
    senha = 'senha'
    _usuario.set_password(senha)
    _usuario.save()
    _usuario.senha_plana = senha
    return _usuario


@pytest.fixture()
def resp_post(client, usuario):
    resp = client.post(reverse('login'), {'username': usuario.email, 'password': usuario.senha_plana})
    return resp


def test_login_redirect(resp_post):
    assert resp_post.status_code == 302
    assert resp_post.url == reverse('modulos:indice')
