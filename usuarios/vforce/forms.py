from django import forms
from .models import Cliente

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente  # Utiliza el modelo Cliente
        fields = '__all__'  # Incluye todos los campos del modelo
    
    def clean_nombre(self):
        nombre = self.cleaned_data['nombre']  # Obtiene el nombre limpio del formulario
        if Cliente.objects.filter(nombre__iexact=nombre).exclude(pk=self.instance.pk).exists():
            raise forms.ValidationError("Este nombre ya está registrado")  # Levanta un error si el nombre ya está registrado
        return nombre  # Devuelve el nombre limpio

    def clean_email(self):
        email = self.cleaned_data.get('email')  # Obtiene el email limpio del formulario
        if Cliente.objects.filter(email__iexact=email).exclude(pk=self.instance.pk).exists():
            raise forms.ValidationError("Este email ya está registrado")  # Levanta un error si el email ya está registrado
        return email  # Devuelve el email limpio

    def clean_telefono(self):
        telefono = self.cleaned_data.get('telefono')  # Obtiene el teléfono limpio del formulario
        if Cliente.objects.filter(telefono__iexact=telefono).exclude(pk=self.instance.pk).exists():
            raise forms.ValidationError("Este teléfono ya está registrado")  # Levanta un error si el teléfono ya está registrado
        return telefono  # Devuelve el teléfono limpio