from django.db import models
from django.contrib.auth.models import User

class Apartamento(models.Model):
    numero = models.CharField(max_length=10, unique=True, help_text="Ex: 101A")
    bloco = models.CharField(max_length=10, blank=True, null=True, help_text="Ex: Bloco Sol")
    
    def __str__(self):
        return f"Apto {self.numero} - Bloco {self.bloco or ''}"

class Morador(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    nome_completo = models.CharField(max_length=255)
    cpf = models.CharField(max_length=14, unique=True)
    telefone = models.CharField(max_length=20, blank=True)
    email = models.EmailField(unique=True)
    apartamento = models.ForeignKey(Apartamento, related_name='moradores', on_delete=models.CASCADE)
    
    def __str__(self):
        return self.nome_completo

class Aviso(models.Model):
    titulo = models.CharField(max_length=200)
    conteudo = models.TextField()
    imagem = models.ImageField(upload_to='avisos/', blank=True, null=True)
    data_criacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo

class Pagamento(models.Model):
    STATUS_CHOICES = [
        ('Pendente', 'Pendente'),
        ('Pago', 'Pago'),
        ('Atrasado', 'Atrasado'),
    ]
    apartamento = models.ForeignKey(Apartamento, on_delete=models.CASCADE, related_name='pagamentos')
    descricao = models.CharField(max_length=200, default='Taxa condominial')
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    data_vencimento = models.DateField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='Pendente')
    data_pagamento = models.DateField(blank=True, null=True)

    def __str__(self):
        return f"{self.descricao} - Apto {self.apartamento.numero} - Venc: {self.data_vencimento}"

class Reserva(models.Model):
    morador = models.ForeignKey(Morador, on_delete=models.CASCADE)
    area_comum = models.CharField(max_length=100, help_text='Ex: Salão de Festas, Churrasqueira')
    data_reserva = models.DateField()
    status = models.CharField(max_length=50, default='Confirmada')

    def __str__(self):
        return f"{self.area_comum} - {self.morador.nome_completo} em {self.data_reserva}"