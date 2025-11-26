<<<<<<< HEAD
from django.shortcuts import render, redirect
=======
from django.shortcuts import render, redirect, get_object_or_404
>>>>>>> e5f396d171b77b490a6417d9dc49a5fc3a638cdb
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from rest_framework import viewsets
<<<<<<< HEAD
from rest_framework.permissions import IsAuthenticated, IsAdminUser 

from .models import Apartamento, Morador, Aviso
=======
from .models import Apartamento, Morador, Aviso, Pagamento, Reserva
>>>>>>> e5f396d171b77b490a6417d9dc49a5fc3a638cdb
from .serializers import ApartamentoSerializer, MoradorSerializer, AvisoSerializer
from .forms import MoradorForm, PagamentoForm


class ApartamentoViewSet(viewsets.ModelViewSet):
    queryset = Apartamento.objects.all().order_by('bloco', 'numero')
    serializer_class = ApartamentoSerializer
    permission_classes = [IsAdminUser] 

class MoradorViewSet(viewsets.ModelViewSet):
    queryset = Morador.objects.all().order_by('nome_completo')
    serializer_class = MoradorSerializer
    permission_classes = [IsAdminUser]

class AvisoViewSet(viewsets.ModelViewSet):
    queryset = Aviso.objects.all().order_by('-data_criacao')
    serializer_class = AvisoSerializer
<<<<<<< HEAD
    permission_classes = [IsAuthenticated]


=======
>>>>>>> e5f396d171b77b490a6417d9dc49a5fc3a638cdb

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
        messages.error(request, 'Usuário ou senha inválidos.')
    else:
        form = AuthenticationForm()
    return render(request, 'core/login.html', {'form': form})

def cadastro_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Cadastro realizado com sucesso! Faça login.')
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'core/cadastro.html', {'form': form})

def logout_view(request):
    logout(request)
    messages.info(request, 'Você saiu da sua conta.')
    return redirect('login')

@login_required(login_url='login')
def home(request):
    lista_de_avisos = Aviso.objects.all().order_by('-data_criacao')[:5]
    contexto = {'avisos': lista_de_avisos}
    return render(request, 'core/home.html', contexto)

@login_required(login_url='login')
def moradores(request):
    if not request.user.is_superuser:
        messages.warning(request, 'Você não tem permissão para acessar esta página.')
        return redirect('home')
    lista_de_moradores = Morador.objects.all().order_by('nome_completo')
    contexto = {'moradores': lista_de_moradores}
    return render(request, 'core/moradores.html', contexto)

@login_required(login_url='login')
def morador_adicionar(request):
    if not request.user.is_superuser:
        messages.warning(request, 'Você não tem permissão para realizar esta ação.')
        return redirect('home')
    if request.method == 'POST':
        form = MoradorForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Morador adicionado com sucesso!')
            return redirect('moradores')
    else:
        form = MoradorForm()
    contexto = {'form': form}
    return render(request, 'core/morador_form.html', contexto)

@login_required(login_url='login')
def financeiro(request):
    if request.user.is_superuser:
        lista_de_pagamentos = Pagamento.objects.all().order_by('-data_vencimento')
    else:
        try:
            morador = Morador.objects.get(user=request.user)
            lista_de_pagamentos = Pagamento.objects.filter(apartamento=morador.apartamento).order_by('-data_vencimento')
        except Morador.DoesNotExist:
            lista_de_pagamentos = []
            messages.warning(request, 'Seu usuário não está associado a nenhum morador.')
    contexto = {'pagamentos': lista_de_pagamentos}
    return render(request, 'core/financeiro.html', contexto)

@login_required(login_url='login')
def pagamento_adicionar(request):
    if not request.user.is_superuser:
        messages.warning(request, 'Você não tem permissão para realizar esta ação.')
        return redirect('home')
    if request.method == 'POST':
        form = PagamentoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Lançamento financeiro adicionado com sucesso!')
            return redirect('financeiro')
    else:
        form = PagamentoForm()
    contexto = {'form': form}
    return render(request, 'core/pagamento_form.html', contexto)

@login_required(login_url='login')
def reservas(request):
    if request.user.is_superuser:
        lista_de_reservas = Reserva.objects.all().order_by('-data_reserva')
    else:
        try:
            morador = Morador.objects.get(user=request.user)
            lista_de_reservas = Reserva.objects.filter(morador=morador).order_by('-data_reserva')
        except Morador.DoesNotExist:
            lista_de_reservas = []
    contexto = {'reservas': lista_de_reservas}
    return render(request, 'core/reservas.html', contexto)

@login_required(login_url='login')
def avisos(request):
    lista_de_avisos = Aviso.objects.all().order_by('-data_criacao')
    contexto = {'avisos': lista_de_avisos}
    return render(request, 'core/avisos.html', contexto)

@login_required(login_url='login')
def aviso_deletar(request, pk):
    if not request.user.is_superuser:
        messages.warning(request, 'Você não tem permissão para realizar esta ação.')
        return redirect('home')
    aviso = get_object_or_404(Aviso, pk=pk)
    if request.method == 'POST':
        aviso.delete()
        messages.success(request, 'Aviso deletado com sucesso!')
        return redirect('avisos')
    contexto = {'aviso': aviso}
    return render(request, 'core/aviso_confirm_delete.html', contexto)