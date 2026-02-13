import logging
# from infra.notificadores.base import NotificadorBase

class NotificadorMock:
    def enviar_confirmacion_orden(self, numero_orden: str, total: str, email: str) -> None:
        logging.info("MOCK: Orden %s, total %s, email %s", numero_orden, total, email)
        # o print(...) para verlo en consola