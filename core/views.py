from django.shortcuts import render, redirect
from .models import *
from .forms import ProductoForm, RegistroUsuarioForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required, user_passes_test

#PERMISOS DE USUARIO
def grupo_requerido(nombre_grupo):
    def decorator(view_fuc):
        @user_passes_test(lambda user: user.groups.filter(name=nombre_grupo).exists())
        def wrapper(request, *args, **kwargs):
            return view_fuc(request, *args, **kwargs)
        return wrapper
    return decorator

# @grupo_requerido('admin')




# Create your views here.
@login_required
def index(request):
    return render(request, 'core/index.html')
@login_required
def about(request):
    return render(request, 'core/about.html')
@login_required
def contact(request):
    return render(request, 'core/contact.html')

@login_required
def cart(request):
    return render(request, 'core/cart.html')
@login_required
def cuenta(request):
    return render(request, 'core/crud/cuenta.html')
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

@login_required
def panel(request):
    ProductoAll = Producto.objects.all() 
    data = {
        'listaProductos' : ProductoAll

    }

    return render(request, 'core/crud/panel.html', data)



#CRUD
@login_required
def shop(request):
    ProductoAll = Producto.objects.all() 
    data = {
        'listaProductos' : ProductoAll

    }

    return render(request, 'core/shop.html', data)

#AGREGAR
@login_required
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
    return render (request, 'core/crud/agregar.html', data)

#MODIFICAR
@login_required
def actualizar(request,id):
    producto = Producto.objects.get(id=id)
    data = {
        'form' :ProductoForm(instance=producto)
    }
    
    if request.method == 'POST':
        formulario = ProductoForm(data=request.POST,instance=producto, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "actualizado correctamente")
            data['mensaje'] = "Actualizado correctamente" 
        else:
            data['form'] = formulario
        
    
    return render(request, 'core/crud/actualizar.html', data)

#ELIMINAR
@login_required
def eliminar(request,id):
    producto = Producto.objects.get(id=id)
    producto.delete()

    return redirect(to="panel")
#BUSCAR
@login_required
def buscar(request):
    query = request.GET.get('q', '')
    productos = []
    if query:
        productos = Producto.objects.filter(nombre__icontains=query)
    
    context = {
        'productos': productos,
        'query': query,
    }
    return render(request, 'core/buscar.html', context)