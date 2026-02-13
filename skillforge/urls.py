"""
URL configuration for skillforge project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.catalog, name="catalog"),
    path("carrito/", views.carrito_view, name="carrito"),
    path("carrito/add/", views.add_to_cart, name="add_to_cart"),
    path("carrito/checkout/", views.checkout, name="checkout"),
    path("orden_ok/<str:numero>/", views.orden_ok, name="orden_ok"),
]
