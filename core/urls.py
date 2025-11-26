from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView 

from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from . import views 


router = DefaultRouter()
router.register(r'apartamentos', views.ApartamentoViewSet)
router.register(r'moradores', views.MoradorViewSet)
router.register(r'avisos', views.AvisoViewSet)


urlpatterns = [
    #  Rotas da Aplicação (HTML Views)
    path('', views.home, name='home'),
    path('login/', views.login_view, name='login'),
    path('cadastro/', views.cadastro_view, name='cadastro'),
    path('logout/', views.logout_view, name='logout'),
    path('moradores/', views.moradores, name='moradores'),
    path('moradores/adicionar/', views.morador_adicionar, name='morador_adicionar'),
    path('financeiro/', views.financeiro, name='financeiro'),
    path('reservas/', views.reservas, name='reservas'),
    path('avisos/', views.avisos, name='avisos'),
    
    
    
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'), # Login: Retorna token de acesso
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'), # Renova o token de acesso
    
    
    # 3. Rotas para Documentação (Swagger/OpenAPI)
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'), # O arquivo de definição do Schema
    path('api/schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'), 
    
    
  
    path('api/', include(router.urls)),
]