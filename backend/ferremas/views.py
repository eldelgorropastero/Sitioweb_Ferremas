from django.shortcuts import render, redirect
from .models import Usuario, Producto
from django.contrib import messages

# Registro básico
def registro(request):
    if request.method == 'POST':
        nombre = request.POST['nombre_completo']
        correo = request.POST['correo_electronico']
        contraseña = request.POST['contraseña']
        if Usuario.objects.filter(correo_electronico=correo).exists():
            messages.error(request, 'Correo ya registrado')
            return redirect('registro')
        nuevo_usuario = Usuario(nombre_completo=nombre, correo_electronico=correo, contraseña=contraseña)
        nuevo_usuario.save()
        messages.success(request, 'Usuario registrado correctamente')
        return redirect('login')
    return render(request, 'registro.html')

# Inicio de sesión básico
def login(request):
    if request.method == 'POST':
        correo = request.POST['correo_electronico']
        contraseña = request.POST['contraseña']
        try:
            usuario = Usuario.objects.get(correo_electronico=correo, contraseña=contraseña)
            request.session['usuario_id'] = str(usuario.id_usuario)  
            return redirect('productos')
        except Usuario.DoesNotExist:
            messages.error(request, 'Credenciales incorrectas')
            return redirect('login')
    return render(request, 'login.html')


def productos(request):
    if 'usuario_id' not in request.session:
        messages.error(request, 'Debes iniciar sesión para ver los productos')
        return redirect('login')
    productos = Producto.objects.all()
    return render(request, 'productos.html', {'productos': productos})

