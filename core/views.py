
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from rest_framework import viewsets


from .models import Apartamento, Morador, Aviso
from .serializers import ApartamentoSerializer, MoradorSerializer, AvisoSerializer
from .forms import MoradorForm 



class ApartamentoViewSet(viewsets.ModelViewSet):
    queryset = Apartamento.objects.all()
    serializer_class = ApartamentoSerializer

class MoradorViewSet(viewsets.ModelViewSet):
    queryset = Morador.objects.all()
    serializer_class = MoradorSerializer

class AvisoViewSet(viewsets.ModelViewSet):
    queryset = Aviso.objects.all()
    serializer_class = AvisoSerializer




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
            else:
                messages.error(request, 'Usuário ou senha inválidos.')
        else:
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
# -----------------------------

@login_required(login_url='login')
def financeiro(request):
    return render(request, 'core/financeiro.html')

@login_required(login_url='login')
def reservas(request):
    return render(request, 'core/reservas.html')

@login_required(login_url='login')
def avisos(request):
    lista_de_avisos = Aviso.objects.all().order_by('-data_criacao')
    contexto = {'avisos': lista_de_avisos}
    return render(request, 'core/avisos.html', contexto)

def sobre(request):
    return render(request, 'sobre.html')

def contato(request):
    return render(request, 'contato.html')