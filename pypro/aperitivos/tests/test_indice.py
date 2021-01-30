import pytest
from django.urls import reverse
from pypro.django_assertions import assert_contains
from pypro.aperitivos.models import Video
from model_bakery import baker


@pytest.fixture()
def videos(db):
    return baker.make(Video, 3)


@pytest.fixture()
def resp(client, videos):
    return client.get(reverse('aperitivos:index'))


def test_status_code(resp):
    return resp.status_code == 200


def test_video_title(resp, videos):
    for video in videos:
        assert_contains(resp, video.titulo)


def test_video_link(resp, videos):
    for video in videos:
        video_link = reverse('aperitivos:video', args=(video.slug,))
        assert_contains(resp, f'href="{video_link}"')
