from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name="home" ),
    path('productos/', views.productos, name="producto"),
    path('ventas/', views.ventas, name="venta"),
    path('clientes/', views.clientes, name="cliente"),
]


