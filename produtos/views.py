from django.shortcuts import render

# Create your views here.
def produtos(request):
    contexto = {
        'title' : 'Produtos '
    }
    return render(
        request,
        'produtos/index.html',
        contexto
    )
