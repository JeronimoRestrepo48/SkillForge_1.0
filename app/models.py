from django.db import models
from decimal import Decimal


class Curso(models.Model):
    nombre = models.CharField(max_length=200)
    precio = models.DecimalField(max_digits=10, decimal_places=2, default=Decimal("0"))
    descripcion = models.TextField(blank=True)

    class Meta:
        verbose_name_plural = "Cursos"

    def __str__(self):
        return self.nombre


class Carrito(models.Model):
    session_key = models.CharField(max_length=40, unique=True, null=True, blank=True)
    creado = models.DateTimeField(auto_now_add=True)

    def items_all(self):
        return self.carritoitem_set.select_related("curso").all()

    def __str__(self):
        return f"Carrito {self.session_key or self.pk}"


class CarritoItem(models.Model):
    carrito = models.ForeignKey(Carrito, on_delete=models.CASCADE)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField(default=1)

    class Meta:
        unique_together = [("carrito", "curso")]

    def __str__(self):
        return f"{self.cantidad} x {self.curso.nombre}"
