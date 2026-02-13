# from infra.notificadores.base import NotificadorBase

class NotificadorReal:
    def enviar_confirmacion_orden(self, numero_orden: str, total: str, email: str) -> None:
        # Enviar email real (SMTP, SendGrid, etc.)
        pass