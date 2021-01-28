import pytest
from django.urls import reverse
from pypro.django_assertions import assert_contains


@pytest.fixture()
def resp(client, db):
    return client.get(reverse('aperitivos:video', args=('motivacao',)))


def test_status_code(resp):
    return resp.status_code == 200


def test_video_title(resp):
    assert_contains(resp, '<h1>Video Aperitivo: Motivação</h1>')


def test_video_conteudo(resp):
    assert_contains(resp, '<iframe src="https://player.vimeo.com/video/501491219"')
