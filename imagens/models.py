from django.db import models

# Create your models here.
from django.db import models

class Imagem(models.Model):
    titulo = models.CharField(max_length=255)
    imagem = models.ImageField(upload_to='imagens/')
    descricao = models.TextField(blank=True)

    def __str__(self):
        return self.titulo
