from django.urls import path, include
from .views import *
from rest_framework import routers

router = routers.DefaultRouter()
router.register('productos', ProductoViewset)
urlpatterns = [

    #APIS
    path('api/', include(router.urls)),
    path('Apis/', Apis, name="Apis"),
    path('api_proyecto/', api_proyecto, name="api_proyecto"),

    #RUTAS
    path('', index, name="index"),
    path('about', about, name="about"),
    path('cart', cart, name="cart"),
    path('contact', contact, name="contact"),
    path('shop', shop, name="shop"),
    path('register/', register, name="register"),
    path('panel/', panel, name="panel"),
    path('cuenta/', cuenta, name="cuenta"),
   

    path('agregar/', agregar, name="agregar"),
    path('actualizar/<codigo_producto>/', actualizar, name="actualizar"),
    path('eliminar/<codigo_producto>/', eliminar, name="eliminar"),
    path('buscar/', buscar, name='buscar'),


    #CARRITO
    path('cart', cart, name="cart"),
    path('vaciar_carrito/', vaciar_carrito, name='vaciar_carrito'),
    path('eliminar_carrito/<codigo_producto>/', eliminar_carrito, name='eliminar_carrito'),
    path('aumentar_cantidad/<codigo_producto>/', aumentar_cantidad, name='aumentar_cantidad'),
    path('disminuir_cantidad/<codigo_producto>/', disminuir_cantidad, name='disminuir_cantidad'),
  
]
