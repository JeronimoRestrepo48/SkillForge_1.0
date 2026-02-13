# checkout_app/services.py
class CheckoutService:
    def __init__(self, notificador=None):
        self.notificador = notificador or NotificadorFactory.get_notificador()

    def ejecutar_checkout(self, user) -> Orden | None:
        carrito = obtener_o_crear_carrito(user)
        items = carrito.items_all()
        if not items:
            return None
        with transaction.atomic():
            builder = OrderBuilder().para_usuario(user).con_numero(_generar_numero_orden())
            for item in items:
                builder.con_item(item.curso, item.curso.precio, item.cantidad)
            orden = builder.build()
            vaciar_carrito(carrito)
        self.notificador.enviar_confirmacion_orden(orden.numero_orden, str(orden.total), user.email or '')
        return orden