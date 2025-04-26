from django.db import models

class Produto(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    imagem = models.ImageField(upload_to='produtos/')

    def __str__(self):
        return self.nome

