
from django import forms
from .models import Morador
from .models import Morador, Pagamento

class LoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput) 


class MoradorForm(forms.ModelForm):
    class Meta:
        model = Morador
        fields = ['nome_completo', 'cpf', 'email', 'telefone', 'apartamento']


class PagamentoForm(forms.ModelForm):
    class Meta:
        model = Pagamento
        fields = ['apartamento', 'descricao', 'valor', 'data_vencimento']        
