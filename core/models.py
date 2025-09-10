# core/models.py

from django.db import models

class Apartamento(models.Model):
    numero = models.CharField(max_length=10, unique=True, help_text="Ex: 101A")
    bloco = models.CharField(max_length=10, blank=True, null=True, help_text="Ex: Bloco Sol")
    
    def __str__(self):
        return f"Apto {self.numero} - Bloco {self.bloco or ''}"

class Morador(models.Model):
    nome_completo = models.CharField(max_length=255)
    cpf = models.CharField(max_length=14, unique=True)
    telefone = models.CharField(max_length=20, blank=True)
    email = models.EmailField(unique=True)
    

    apartamento = models.ForeignKey(Apartamento, related_name='moradores', on_delete=models.CASCADE)
    
    def __str__(self):
        return self.nome_completo

class Aviso(models.Model):
    titulo = models.CharField(max_length=200)
    conteudo = models.TextField(help_text="Descreva o aviso aqui.")
    imagem = models.ImageField(upload_to='avisos/', blank=True, null=True, help_text="Anexe uma imagem se necessário.")
    data_criacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo