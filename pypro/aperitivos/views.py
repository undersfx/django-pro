from django.shortcuts import render, get_object_or_404
from pypro.aperitivos.models import Video


def video(request, slug):
    video = get_object_or_404(Video, slug=slug)
    return render(request, 'aperitivos/video.html', context={'video': video})


def index(request):
    # TODO: Refactorar regra de negócio para um modulo de fachada (facade).
    videos = Video.objects.order_by('creation').all()
    return render(request, 'aperitivos/index.html', context={'videos': videos})
