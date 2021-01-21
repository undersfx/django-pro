import pytest
from django.urls import reverse
from pypro.django_assertions import assert_contains


@pytest.fixture()
def resp(client):
    return client.get(reverse('aperitivos:index'))


def test_status_code(resp):
    return resp.status_code == 200


@pytest.mark.parametrize(
    'titulo', [
        'Video Aperitivo: Motivação',
        'Video Aperitivo: Instalação Windows'
    ]
)
def test_video_title(resp, titulo):
    assert_contains(resp, titulo)
