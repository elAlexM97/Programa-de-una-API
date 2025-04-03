from django.shortcuts import render, redirect, get_object_or_404  # Importa funciones útiles de Django
from vforce.models import Cliente  # Importa el modelo Cliente
from vforce.forms import ClienteForm  # Importa el formulario ClienteForm
from django.http import JsonResponse  # Importa la función JsonResponse
    
    
def lista_clientes(request):
    clientes = Cliente.objects.all()  # Obtiene todos los clientes
    return render(request, 'vforce/lista_clientes.html', {'clientes': clientes})  # Renderiza la lista de clientes

def crear_cliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)  # Crea un formulario con los datos enviados
        if form.is_valid():
            form.save()  # Guarda el nuevo cliente
            return redirect('lista_clientes')  # Redirige a la lista de clientes
    else:
        form = ClienteForm()  # Crea un formulario vacío
    return render(request, 'vforce/crear_cliente.html', {'form': form})  # Renderiza la página para crear un cliente

def editar_cliente(request, id):
    cliente = get_object_or_404(Cliente, id=id)  # Obtiene el cliente por ID, o muestra error 404 si no existe
    if request.method == 'POST':
        form = ClienteForm(request.POST, instance=cliente)  # Crea un formulario con los datos enviados y el cliente existente
        if form.is_valid():
            form.save()  # Guarda los cambios del cliente
            return redirect('lista_clientes')  # Redirige a la lista de clientes
    else:
        form = ClienteForm(instance=cliente)  # Crea un formulario con los datos del cliente existente
    return render(request, 'vforce/editar_cliente.html', {'form': form})  # Renderiza la página para editar un cliente

def eliminar_cliente(request, id):
    cliente = get_object_or_404(Cliente, id=id)  # Obtiene el cliente por ID, o muestra error 404 si no existe
    if request.method == 'POST':
        cliente.delete()  # Elimina el cliente
        return redirect('lista_clientes')  # Redirige a la lista de clientes
    return render(request, 'vforce/eliminar_cliente.html', {'form': cliente})  # Renderiza la página para confirmar eliminación

def check_email(request):
    email = request.GET.get('email', '')  # Obtiene el email de la solicitud
    exists = Cliente.objects.filter(email__iexact=email).exists()  # Verifica si el email ya existe
    return JsonResponse({'exists': exists})  # Devuelve un JSON con el resultado

def check_telefono(request):
    telefono = request.GET.get('telefono', '')  # Obtiene el teléfono de la solicitud
    exists = Cliente.objects.filter(telefono__iexact=telefono).exists()  # Verifica si el teléfono ya existe
    return JsonResponse({'exists': exists})  # Devuelve un JSON con el resultado

def check_nombre(request):
    nombre = request.GET.get('nombre', '')  # Obtiene el nombre de la solicitud
    exists = Cliente.objects.filter(nombre__iexact=nombre).exists()  # Verifica si el nombre ya existe
    return JsonResponse({'exists': exists})  # Devuelve un JSON con el resultado

def check_duplicate(request):
    field = request.GET.get('field')  # Obtiene el campo a verificar
    