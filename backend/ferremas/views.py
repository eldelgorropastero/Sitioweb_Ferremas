from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import Producto
from .serializers import ProductoSerializer

def index(request):
    return render(request, 'Ferremas/index.html')

def page_producto(request):
    return render(request, 'Ferremas/productos.html')

def page_contacto(request):
    return render(request, 'Ferremas/contacto.html')

class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer