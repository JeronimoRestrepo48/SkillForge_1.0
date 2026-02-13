# domain/order.py
from dataclasses import dataclass
from decimal import Decimal
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from django.contrib.auth import get_user_model
    User = get_user_model()

@dataclass(frozen=True)  # opcional: inmutable
class OrderItem:
    curso_id: int
    precio: Decimal
    cantidad: int
    subtotal: Decimal  # precio * cantidad

@dataclass
class Orden:
    numero_orden: str
    user_id: int
    items: list[OrderItem]
    total: Decimal

    def __post_init__(self):
        if not self.numero_orden or not self.numero_orden.strip():
            raise ValueError("Orden debe tener numero_orden")
        if not self.items:
            raise ValueError("Orden debe tener al menos un ítem")
        if self.total < 0:
            raise ValueError("Orden total no puede ser negativo")