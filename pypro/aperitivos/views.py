from django.shortcuts import render
from django.urls import reverse


class Video:
    def __init__(self, slug, titulo, vimeo_id):
        self.slug = slug
        self.titulo = titulo
        self.vimeo_id = vimeo_id

    def get_absolute_url(self):
        return reverse('aperitivos:video', args=(self.slug,))


videos = [
    Video('motivacao', 'Video Aperitivo: Motivação', '501491219'),
    Video('instalacao', 'Video Aperitivo: Instalação Windows', '502404083')
]

videos_dct = {v.slug: v for v in videos}


def video(request, slug):
    video = videos_dct[slug]
    return render(request, 'aperitivos/video.html', context={'video': video})


def index(request):
    return render(request, 'aperitivos/index.html', context={'videos': videos})
