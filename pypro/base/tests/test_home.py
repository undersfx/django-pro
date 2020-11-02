import pytest
from django.test import Client
from pypro.django_assertions import assert_contains
from django.urls import reverse

@pytest.fixture()
def resp(client):
    resp = client.get(reverse('home'))
    return resp

def test_status_code(resp):
    assert resp.status_code == 200

def test_home_title(resp):
    assert_contains(resp, '<title>Python Pro</title>')

def test_home_redirect(resp):
    assert_contains(resp, f'href="{reverse("home")}">Python Pro</a>')
