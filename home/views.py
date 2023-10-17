from django.shortcuts import render

# Create your views here.
def home(request):
    contexto = {
        'title' : 'Home '
    }
    return render(
        request,
        'home/index.html',
        contexto
    )