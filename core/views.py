from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# LOGIN
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')  # Redireciona para a página inicial após o login
            else:
                form.add_error(None, 'Usuário ou senha inválidos.')
    else:
        form = AuthenticationForm()
    return render(request, 'core/login.html', {'form': form})

# CADASTRO
def cadastro_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Cadastro realizado com sucesso! Faça login.')
            return redirect('login')  # Redireciona para a página de login após o cadastro
        else:
            messages.error(request, 'Erro ao cadastrar. Verifique os dados.')
    else:
        form = UserCreationForm()
    return render(request, 'core/cadastro.html', {'form': form})

# LOGOUT
def logout_view(request):
    logout(request)
    return redirect('login')  # Redireciona para a página de login após o logout

# PÁGINAS PROTEGIDAS
@login_required(login_url='login')  # Garantir que apenas usuários logados acessem
def home(request):
    return render(request, 'core/home.html')

@login_required(login_url='login')
def moradores(request):
    return render(request, 'core/moradores.html')

@login_required(login_url='login')
def financeiro(request):
    return render(request, 'core/financeiro.html')

@login_required(login_url='login')
def reservas(request):
    return render(request, 'core/reservas.html')

@login_required(login_url='login')
def avisos(request):
    return render(request, 'core/avisos.html')

def sobre(request):
    return render(request, 'sobre.html')

def contato(request):
    return render(request, 'contato.html')
