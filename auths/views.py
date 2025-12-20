from urllib import request
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from . import models
from .forms import FormularioRegistro

def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        # Aquí iría la lógica de autenticación
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('app_home:home')  # Redirigir a la página principal después del inicio de sesión exitoso
        else:
            context = {'error': 'Credenciales inválidas. Por favor, inténtalo de nuevo.'}
            return render(request, 'auths/login.html', context)
    return render(request, 'auths/login.html')


def logout_view(request):
    pass

def register_view(request):
    if request.method == 'POST':
        formulario = FormularioRegistro(request.POST) # Se instancia el formulario con los datos enviados por el usuario (capturamos los datos enviados por el usuario en el navegador)
        if formulario.is_valid():
            nombre = formulario.cleaned_data.get('name')
            apellido = formulario.cleaned_data.get('lastname')  
            email = formulario.cleaned_data.get('email')
            password = formulario.cleaned_data.get('password')
            telefono = formulario.cleaned_data.get('phone_number')
            username = email.split('@')[0]
            user=models.Auth.objects.create_user(
                username=username,
                name=nombre,
                lastname=apellido,
                email=email,
                password=password,
            )
            user.phone_number=telefono
            user.save()
            return redirect('auths:login')
    else:
        formulario=FormularioRegistro()
           
    context = {
        'formulario': formulario,
    }
   
    return render(request, 'auths/register.html', context)