from django.shortcuts import render

# Create your views here.
from django.views import View
from django.shortcuts import redirect
from app.services import CheckoutService

def checkout(request):
    """GET: muestra el template en la raíz. POST: ejecuta checkout."""
    if request.method == 'POST':
        orden = CheckoutService().ejecutar_checkout(request.user)
        if orden:
            return redirect('orden_ok', numero=orden.numero_orden)
        return redirect('checkout')
    return render(request, 'index.html')

def orden_ok(request, numero):
    return render(request, 'orden_ok.html', {'numero': numero})