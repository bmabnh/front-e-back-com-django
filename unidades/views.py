from django.shortcuts import render

# Create your views here.
def unidades(request):
    contexto = {
        'title' : 'Unidades '
    }
    return render(
        request,
        'unidades/index.html',
        contexto
    )