import pytest
from django.urls import reverse
from pypro.django_assertions import assert_contains
from pypro.aperitivos.models import Video


@pytest.fixture()
def video(db):
    video_obj = Video(slug='motivacao', titulo='Video Aperitivo: Motivação', vimeo_id='501491219')
    video_obj.save()
    return video_obj


@pytest.fixture()
def resp(client, video):
    return client.get(reverse('aperitivos:video', args=(video.slug,)))


@pytest.fixture()
def resp_video_nao_existente(client, video):
    return client.get(reverse('aperitivos:video', args=(video.slug + '_invalido',)))


def test_status_code(resp):
    return resp.status_code == 200


def test_status_code_nao_existente(resp_video_nao_existente):
    return resp_video_nao_existente.status_code == 404


def test_video_title(resp, video):
    assert_contains(resp, video.titulo)


def test_video_conteudo(resp, video):
    assert_contains(resp, f'<iframe src="https://player.vimeo.com/video/{video.vimeo_id}"')
