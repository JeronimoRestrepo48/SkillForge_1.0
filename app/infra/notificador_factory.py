from django.conf import settings


def get_notificador():
    backend = getattr(settings, "NOTIFICADOR_BACKEND", "MOCK").upper()
    if backend == "REAL":
        from app.infra.notificadores.real import NotificadorReal
        return NotificadorReal()
    from app.infra.notificadores.mock import NotificadorMock
    return NotificadorMock()