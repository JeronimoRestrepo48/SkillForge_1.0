from django.conf import settings

def get_notificador():
    backend = getattr(settings, "NOTIFICADOR_BACKEND", "MOCK")
    if backend == "REAL":
        from infra.notificadores.real import NotificadorReal
        return NotificadorReal()
    # por defecto MOCK
    from infra.notificadores.mock import NotificadorMock
    return NotificadorMock()