from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_imagens, name='lista_imagens'),
]