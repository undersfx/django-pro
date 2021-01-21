from django.urls import path
from pypro.aperitivos.views import video, index


app_name = 'aperitivos'

urlpatterns = [
    path('', index, name='index'),
    path('<slug:slug>', video, name='video'),
]
