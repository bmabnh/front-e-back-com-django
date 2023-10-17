from django.shortcuts import render
from .models import Imagem

def lista_imagens(request):
    imagens = Imagem.objects.all()
    return render(request, 'imagens/lista_imagens.html', {'imagens': imagens})

def lista_imagens(request):
    contexto = {
        'title' : 'imagens '
    }
    return render(
        request,
        'imagens/lista_imagens.html',
        contexto
    )
