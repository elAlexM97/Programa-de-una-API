from django.db import models
from django.core.exceptions import ValidationError

class Cliente(models.Model):
    nombre = models.CharField(max_length=30)
    email = models.EmailField(unique=True)
    telefono = models.CharField(max_length=10)
    fecha_registro = models.DateTimeField(auto_now_add=True)

    def clean(self):
        # Validación adicional para evitar duplicados
        if Cliente.objects.exclude(pk=self.pk).filter(email=self.email).exists():
            raise ValidationError({'email': 'Este email ya está registrado'})
        
        if Cliente.objects.exclude(pk=self.pk).filter(telefono=self.telefono).exists():
            raise ValidationError({'telefono': 'Este teléfono ya está registrado'})

    def __str__(self):
        return self.nombre