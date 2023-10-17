from django.shortcuts import render

# Create your views here.
def cadastro(request):
    contexto = {
        'title' : 'Cadastro '
    }
    return render(
        request,
        'cadastro/index.html',
        contexto
    )