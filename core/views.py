from django.shortcuts import render
from .models import *
from .forms import *

# Create your views here.

def index(request):
    return render(request, 'core/index.html')

def about(request):
    return render(request, 'core/about.html')


def contact(request):
    return render(request, 'core/contact.html')


def cart(request):
    return render(request, 'core/cart.html')

#CRUD
def shop(request):
    ProductoAll = Producto.objects.all() 
    data = {
        'listaProductos' : ProductoAll

    }

    return render(request, 'core/shop.html', data)

#AGREGAR
def agregar(request):

    data = {
        'form' : ProductoForm()
    }

    if request.method == 'POST':
        formulario = ProductoForm(request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            data['mensaje'] = "Guardado correctamente"
            
        else:
            data['form'] = formulario 
    return render (request, 'core/agregar.html', data)