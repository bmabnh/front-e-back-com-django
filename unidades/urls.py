from django.urls import path
from . import views 
urlpatterns = [
    path('', views.unidades, name='unidades'),
]