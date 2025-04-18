# Generated by Django 5.0.2 on 2025-03-15 04:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True  # Indica que esta es la primera migración para la app

    dependencies = [
        # No hay dependencias en esta migración inicial
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',  # Nombre del modelo a crear
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),  # Campo ID automático
                ('nombre', models.CharField(max_length=30)),  # Campo para el nombre del cliente
                ('email', models.EmailField(max_length=254, unique=True)),  # Campo para el correo electrónico, debe ser único
                ('telefono', models.CharField(max_length=10)),  # Campo para el teléfono del cliente
                ('direccion', models.TextField(max_length=50)),  # Campo para la dirección del cliente
                ('fecha_registro', models.DateTimeField(auto_now_add=True)),  # Campo para la fecha de registro, se añade automáticamente
            ],
        ),
    ]