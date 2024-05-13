from django.urls import path, include
from .views import *

urlpatterns = [
    path('', index, name="index"),
    path('about', about, name="about"),
    path('cart', cart, name="cart"),
    path('contact', contact, name="contact"),
    path('shop', shop, name="shop"),
    path('register/', register, name="register"),
    #CRUD 

    path('agregar/', agregar, name="agregar"),
    #path('actualizar/<id>/', actualizar, name="actualizar"),
    #path('eliminar/<id>/', eliminar, name="eliminar"),
]
