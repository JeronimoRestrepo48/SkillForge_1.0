from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from app.models import Curso
from app.services import CheckoutService
from app.carrito import obtener_o_crear_carrito, añadir_al_carrito


def catalog(request):
    cursos = Curso.objects.all()
    return render(request, "index.html", {"cursos": cursos})


def carrito_view(request):
    carrito = obtener_o_crear_carrito(request.session)
    items = carrito.items_all()
    rows = [(item, item.curso.precio * item.cantidad) for item in items]
    total = sum(subtotal for _, subtotal in rows)
    return render(request, "carrito.html", {"rows": rows, "total": total})


def add_to_cart(request):
    if request.method != "POST":
        return redirect("catalog")
    curso_id = request.POST.get("curso_id")
    cantidad = int(request.POST.get("cantidad", 1) or 1)
    if not curso_id:
        return redirect("catalog")
    curso = get_object_or_404(Curso, pk=curso_id)
    añadir_al_carrito(request.session, curso.pk, cantidad=cantidad)
    messages.success(request, f"'{curso.nombre}' añadido al carrito.")
    next_url = request.POST.get("next") or request.GET.get("next") or "carrito"
    return redirect(next_url)


def checkout(request):
    if request.method != "POST":
        return redirect("carrito")
    orden = CheckoutService().ejecutar_checkout(request.user, request.session)
    if orden:
        return redirect("orden_ok", numero=orden.numero_orden)
    messages.warning(request, "El carrito está vacío. Añade cursos antes de confirmar.")
    return redirect("carrito")


def orden_ok(request, numero):
    return render(request, "orden_ok.html", {"numero": numero})
