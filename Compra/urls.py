from django.urls import path
from rest_framework.routers import DefaultRouter
from .viewsets import CompraViewset
router = DefaultRouter()
router.register('views_compra', viewset=CompraViewset, basename='compra_viewset')

urlpatterns = router.urls