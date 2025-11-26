from rest_framework import serializers
from .models import Apartamento, Morador, Aviso


class MoradorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Morador
        fields = ['id', 'nome_completo', 'cpf', 'telefone', 'email', 'apartamento'] 
        


class ApartamentoSerializer(serializers.ModelSerializer):
    moradores = MoradorSerializer(many=True, read_only=True)

    class Meta:
        model = Apartamento
        fields = ['id', 'numero', 'bloco', 'moradores'] 

class AvisoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aviso
        fields = ['id', 'titulo', 'conteudo', 'imagem', 'data_criacao']
        read_only_fields = ['data_criacao']