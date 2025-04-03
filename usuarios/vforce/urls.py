from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_clientes, name='lista_clientes'),  # Ruta raíz de la app, muestra la lista de clientes
    path('crear/', views.crear_cliente, name='crear_cliente'),  # Ruta para crear un nuevo cliente
    path('editar/<int:id>/', views.editar_cliente, name='editar_cliente'),  # Ruta para editar un cliente por ID
    path('eliminar/<int:id>/', views.eliminar_cliente, name='eliminar_cliente'),  # Ruta para eliminar un cliente por ID
]