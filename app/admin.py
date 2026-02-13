from django.contrib import admin
from app.models import Curso, Carrito, CarritoItem


@admin.register(Curso)
class CursoAdmin(admin.ModelAdmin):
    list_display = ("nombre", "precio")


class CarritoItemInline(admin.TabularInline):
    model = CarritoItem
    extra = 0


@admin.register(Carrito)
class CarritoAdmin(admin.ModelAdmin):
    inlines = [CarritoItemInline]
    list_display = ("id", "session_key", "creado")
