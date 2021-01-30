from django.shortcuts import render, get_object_or_404
from pypro.aperitivos.models import Video


videos = [
    Video(slug='motivacao', titulo='Video Aperitivo: Motivação', vimeo_id='501491219'),
    Video(slug='instalacao', titulo='Video Aperitivo: Instalação Windows', vimeo_id='502404083')
]

videos_dct = {v.slug: v for v in videos}


def video(request, slug):
    video = get_object_or_404(Video, slug=slug)
    return render(request, 'aperitivos/video.html', context={'video': video})


def index(request):
    return render(request, 'aperitivos/index.html', context={'videos': videos})
