from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def productos(request):
    return render(request, 'productos.html')

def ventas(request):
    return render(request, 'ventas.html')

def clientes(request):
    return render(request, 'clientes.html')