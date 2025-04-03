from django.db import models
from django.core.exceptions import ValidationError

class Cliente(models.Model):
    nombre = models.CharField(max_length=30)  # Campo de texto para el nombre del cliente
    email = models.EmailField(unique=True)  # Campo de correo electrónico único
    telefono = models.CharField(max_length=10)  # Campo de texto para el teléfono
    fecha_registro = models.DateTimeField(auto_now_add=True)  # Fecha de registro, se añade automáticamente

    def clean(self):
        # Validación adicional para evitar duplicados
        if Cliente.objects.exclude(pk=self.pk).filter(email=self.email).exists():
            raise ValidationError({'email': 'Este email ya está registrado'})  # Levanta un error si el email ya está registrado
        
        if Cliente.objects.exclude(pk=self.pk).filter(telefono=self.telefono).exists():
            raise ValidationError({'telefono': 'Este teléfono ya está registrado'})  # Levanta un error si el teléfono ya está registrado

    def __str__(self):
        return self.nombre  # Devuelve el nombre del cliente como representación del objeto