from django.shortcuts import render, redirect
from .models import *
from .forms import *
from .forms import ProductoForm, RegistroUsuarioForm
from django.contrib import messages
# Create your views here.

def index(request):
    return render(request, 'core/index.html')

def about(request):
    return render(request, 'core/about.html')


def contact(request):
    return render(request, 'core/contact.html')


def cart(request):
    return render(request, 'core/cart.html')

def register(request):
    
    data ={
        'form' : RegistroUsuarioForm()
    }
    
    if request.method == 'POST':
        formulario = RegistroUsuarioForm(data = request.POST)
        if formulario.is_valid():
            formulario.save()
            #user = authenticate(username=formulario.cleaned_data["username"], password = formulario.cleaned_data["password1"])
            #login(request, user)
            messages.success(request, "Te has registrado correctamente")
            
            return redirect(to="index")
        data ["form"] = formulario

    return render(request, 'registration/register.html', data)




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

#MODIFICAR
def actualizar(request,id):
    producto = Producto.objects.get(id=id)
    data = {
        'form' :ProductoForm(instance=producto)
    }
    
    if request.method == 'POST':
        formulario = ProductoForm(data=request.POST,instance=producto, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            #messages.success(request, "modificado correctamente")
            data['mensaje'] = "Actualizado correctamente" 
        else:
            data['form'] = formulario
        
    
    return render(request, 'core/actualizar.html', data)

#ELIMINAR
def eliminar(request,id):
    producto = Producto.objects.get(id=id)
    producto.delete()

    return redirect(to="shop")
    