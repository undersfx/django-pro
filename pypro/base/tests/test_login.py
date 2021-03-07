import pytest
from django.urls import reverse
from model_bakery import baker
from pypro.django_assertions import assert_contains, assert_not_contains


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


@pytest.fixture()
def resp_home(client, db):
    resp = client.get(reverse('base:home'))
    return resp


def test_botao_entrar(resp_home):
    assert_contains(resp_home, 'Entrar')


def test_link_de_login(resp_home):
    assert_contains(resp_home, reverse('login'))


@pytest.fixture()
def resp_home_com_usuario_logado(client_com_usuario_logado, db):
    resp = client_com_usuario_logado.get(reverse('base:home'))
    return resp


def test_botao_entrar_logado(resp_home_com_usuario_logado):
    assert_not_contains(resp_home_com_usuario_logado, 'Entrar')


def test_link_de_login_logado(resp_home_com_usuario_logado):
    assert_not_contains(resp_home_com_usuario_logado, reverse('login'))


def test_botao_sair(resp_home_com_usuario_logado):
    assert_contains(resp_home_com_usuario_logado, 'Sair')


def test_nome_usuario_logado(resp_home_com_usuario_logado, usuario_logado):
    assert_contains(resp_home_com_usuario_logado, usuario_logado.first_name)
