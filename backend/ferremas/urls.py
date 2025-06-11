from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views
from .views import ProductoViewSet

router = DefaultRouter()

router.register('producto', ProductoViewSet)

urlpatterns = [
    path('', views.index, name='index'),
    path('productos/', views.page_producto, name='productos'),
    path('contacto/', views.page_contacto, name='contacto'),
]