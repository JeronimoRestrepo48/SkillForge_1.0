# domain/order_builder.py
from decimal import Decimal
from domain.order import Orden, OrderItem

class OrderBuilder:
    def __init__(self):
        self._numero_orden: str | None = None
        self._user = None
        self._items: list[OrderItem] = []

    def para_usuario(self, user):
        self._user = user
        return self  # Fluent: retorna self

    def con_numero(self, numero: str):
        self._numero_orden = numero
        return self

    def con_item(self, curso, precio, cantidad: int):
        if cantidad <= 0:
            raise ValueError("cantidad debe ser positiva")
        subtotal = Decimal(str(precio)) * cantidad
        self._items.append(OrderItem(
            curso_id=curso.pk,
            precio=Decimal(str(precio)),
            cantidad=cantidad,
            subtotal=subtotal,
        ))
        return self

    def build(self) -> Orden:
        # Garantizar validez antes de crear la Orden
        if not self._numero_orden or not str(self._numero_orden).strip():
            raise ValueError("Falta numero_orden en la orden")
        if not self._user:
            raise ValueError("Falta usuario en la orden")
        if not self._items:
            raise ValueError("La orden debe tener al menos un ítem")

        total = sum(item.subtotal for item in self._items)
        return Orden(
            numero_orden=str(self._numero_orden),
            user_id=self._user.pk,
            items=list(self._items),
            total=total,
        )