# checkout_app/services.py
from django.db import transaction
from app.infra.notificador_factory import get_notificador
from app.domain.order_builder import OrderBuilder
from app.domain.order import Orden
from app.carrito import (
    obtener_o_crear_carrito,
    vaciar_carrito,
    _generar_numero_orden,
)


class _GuestUser:
    pk = 0
    email = ""


def _user_for_checkout(user):
    if user.is_authenticated:
        return user
    return _GuestUser()


class CheckoutService:
    def __init__(self, notificador=None):
        self.notificador = notificador or get_notificador()

    def ejecutar_checkout(self, user, session) -> Orden | None:
        carrito = obtener_o_crear_carrito(session)
        items = list(carrito.items_all())
        if not items:
            return None
        user_for_order = _user_for_checkout(user)
        with transaction.atomic():
            builder = OrderBuilder().para_usuario(user_for_order).con_numero(_generar_numero_orden())
            for item in items:
                builder.con_item(item.curso, item.curso.precio, item.cantidad)
            orden = builder.build()
            vaciar_carrito(carrito)
        self.notificador.enviar_confirmacion_orden(orden.numero_orden, str(orden.total), user_for_order.email or "")
        return orden