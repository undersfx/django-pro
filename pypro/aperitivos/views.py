from django.shortcuts import render


def video(request, slug):
    videos = {
        'motivacao': {'titulo': 'Video Aperitivo: Motivação', 'vimeo_id': '501491219'},
        'instalacao': {'titulo': 'Video Aperitivo: Instalação Windows', 'vimeo_id': '502404083'}
    }
    contexto = videos[slug]
    return render(request, 'aperitivos/video.html', context={'video': contexto})
