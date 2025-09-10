from rest_framework import serializers
from .models import Apartamento, Morador, Aviso

class ApartamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Apartamento
        fields = ['id', 'numero', 'bloco', 'moradores']

class MoradorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Morador
        fields = ['id', 'nome_completo', 'cpf', 'telefone', 'email', 'apartamento']

class AvisoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aviso
        fields = ['id', 'titulo', 'conteudo', 'imagem', 'data_criacao']