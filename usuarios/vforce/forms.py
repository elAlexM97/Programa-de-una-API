from django import forms
from .models import Cliente

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = '__all__'
        
    def clean_nombre(self):
        nombre = self.cleaned_data['nombre']
        if Cliente.objects.filter(nombre__iexact=nombre).exclude(pk=self.instance.pk).exists():
            raise forms.ValidationError("Este nombre ya está registrado")
        return nombre

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if Cliente.objects.filter(email__iexact=email).exclude(pk=self.instance.pk).exists():
            raise forms.ValidationError("Este email ya está registrado")
        return email

    def clean_telefono(self):
        telefono = self.cleaned_data.get('telefono')
        if Cliente.objects.filter(telefono__iexact=telefono).exclude(pk=self.instance.pk).exists():
            raise forms.ValidationError("Este teléfono ya está registrado")
        return telefono