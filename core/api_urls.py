from rest_framework.routers import DefaultRouter
from .views import ApartamentoViewSet, MoradorViewSet, AvisoViewSet


router = DefaultRouter()


router.register(r'apartamentos', ApartamentoViewSet, basename='apartamento')
router.register(r'moradores', MoradorViewSet, basename='morador')
router.register(r'avisos', AvisoViewSet, basename='aviso')

urlpatterns = router.urls