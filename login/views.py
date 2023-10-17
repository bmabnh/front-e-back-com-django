from django.shortcuts import render

# Create your views here.
def login(request):
    contexto = {
        'title' : 'Login '
    }
    return render(
        request,
        'login/index.html',
        contexto
    )