from django.shortcuts import render, redirect, get_object_or_404
from vforce.models import Cliente
from vforce.forms import ClienteForm
from django.http import JsonResponse
    
    
def lista_clientes(request):
    clientes = Cliente.objects.all()
    return render(request, 'vforce/lista_clientes.html', {'clientes': clientes})

def crear_cliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_clientes')
    else:
        form = ClienteForm()
    return render(request, 'vforce/crear_cliente.html', {'form': form})

def editar_cliente(request, id):
    cliente = get_object_or_404(Cliente, id=id)
    if request.method == 'POST':
        form = ClienteForm(request.POST, instance=cliente)
        if form.is_valid():
            form.save()
            return redirect('lista_clientes')
    else:
        form = ClienteForm(instance=cliente)
    return render(request, 'vforce/editar_cliente.html', {'form': form})

def eliminar_cliente(request, id):
    cliente = get_object_or_404(Cliente, id=id)
    if request.method == 'POST':
        cliente.delete()
        return redirect('lista_clientes')
    return render(request, 'vforce/eliminar_cliente.html', {'form': cliente})

def check_email(request):
    email = request.GET.get('email', '')
    exists = Cliente.objects.filter(email__iexact=email).exists()
    return JsonResponse({'exists': exists})

def check_telefono(request):
    telefono = request.GET.get('telefono', '')
    exists = Cliente.objects.filter(telefono__iexact=telefono).exists()
    return JsonResponse({'exists': exists})

def check_nombre(request):
    nombre = request.GET.get('nombre', '')
    exists = Cliente.objects.filter(nombre__iexact=nombre).exists()
    return JsonResponse({'exists': exists})


def check_duplicate(request):
    field = request.GET.get('field')
    value = request.GET.get('value')
    exclude_id = request.GET.get('exclude_id', None)
    
    filters = {f"{field}__iexact": value}
    if exclude_id:
        filters['id__ne'] = exclude_id
    
    exists = Cliente.objects.filter(**filters).exists()
    return JsonResponse({'exists': exists})