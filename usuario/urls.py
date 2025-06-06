from rest_framework.routers import DefaultRouter
from .viewsets import UsuarioViewset
router = DefaultRouter()

router.register('view_usuario', viewset= UsuarioViewset, basename='usuarios')

urlpatterns = router.urls