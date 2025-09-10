# core/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login_view, name='login'),
    path('cadastro/', views.cadastro_view, name='cadastro'),
    path('logout/', views.logout_view, name='logout'),
    path('moradores/', views.moradores, name='moradores'),
    path('moradores/adicionar/', views.morador_adicionar, name='morador_adicionar'),
    path('financeiro/', views.financeiro, name='financeiro'),
    path('reservas/', views.reservas, name='reservas'),
    path('avisos/<int:pk>/deletar/', views.aviso_deletar, name='aviso_deletar'),
    path('financeiro/lancar/', views.pagamento_adicionar, name='pagamento_adicionar'),
    path('avisos/', views.avisos, name='avisos'),
]