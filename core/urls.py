from django.urls import path, include
from .views import *

urlpatterns = [
    path('', index, name="index"),
    path('about', about, name="about"),
    path('cart', cart, name="cart"),
    path('contact', contact, name="contact"),
    path('shop', shop, name="shop"),
]
