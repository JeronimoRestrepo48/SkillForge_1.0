from app.models import Carrito, CarritoItem
import uuid


def _get_or_create_session_key(session):
    if not session.session_key:
        session.create()
    return session.session_key


def obtener_o_crear_carrito(session):
    key = _get_or_create_session_key(session)
    carrito, _ = Carrito.objects.get_or_create(
        session_key=key,
        defaults={},
    )
    return carrito


def vaciar_carrito(carrito):
    CarritoItem.objects.filter(carrito=carrito).delete()


def añadir_al_carrito(session, curso_id, cantidad=1):
    from app.models import Curso
    carrito = obtener_o_crear_carrito(session)
    curso = Curso.objects.get(pk=curso_id)
    item, created = CarritoItem.objects.get_or_create(
        carrito=carrito,
        curso=curso,
        defaults={"cantidad": cantidad},
    )
    if not created:
        item.cantidad += cantidad
        item.save(update_fields=["cantidad"])
    return item


def _generar_numero_orden():
    return f"ORD-{uuid.uuid4().hex[:8].upper()}"
