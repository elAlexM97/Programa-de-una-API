"""
URL configuration for usuarios project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),  # Ruta para el panel de administración
    path('', include('vforce.urls')),  # Incluye las URLs de la app vforce
    path('check_email/', views.check_email, name='check_email'),  # Ruta para verificar si el email ya está registrado
    path('check_telefono/', views.check_telefono, name='check_telefono'),  # Ruta para verificar si el teléfono ya está registrado
    path('check_duplicate/', views.check_duplicate, name='check_duplicate'),  # Ruta para verificar duplicados
    path('check_nombre/', views.check_nombre, name='check_nombre')  # Ruta para verificar si el nombre ya está registrado
]