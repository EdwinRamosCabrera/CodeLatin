from django.contrib import messages
from django.shortcuts import redirect, render
from django.contrib import auth
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required  
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import EmailMessage,EmailMultiAlternatives
from django.utils.html import strip_tags
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from . import models
from .forms import FormularioRegistro


def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        # Aquí iría la lógica de autenticación
        user = auth.authenticate(request, email=email, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('home:home')  # Redirigir a la página principal después del inicio de sesión exitoso
        else:
            messages.error(request, 'Credenciales inválidas. Por favor, inténtalo de nuevo.')
            return redirect('auths:login')
    return render(request, 'auths/login.html')


def logout_view(request):
    auth.logout(request)
    messages.success(request, "Has cerrado sesión exitosamente.")
    return redirect('auths:login')  # Redirigir a la página principal después del cierre de sesión

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
                is_active=False, # La cuenta se crea como inactiva hasta que se verifique el correo
            )
            user.phone_number=telefono
            user.save()
            # VALIDACIÓN DE CORREO ELECTRÓNICO - ACTIVACIÓN DE CUENTA
            current_site = get_current_site(request) # Obtiene el dominio del sitio actual (tienda.com), variable qu esta en el sitio actual
            body_email = "Hola, debes activar tu cuenta para poder acceder al sistema." # creamos el cuerpo del correo
            message = render_to_string("auths/verify_account.html", { # Plantilla de correo de activación - convierte la plantilla en un string
                'user': user, # Indicamos a que usaurio va dirigido el correo
                'domain': current_site.domain, # Indicamos el dominio del sitio actual
                'uid': urlsafe_base64_encode(force_bytes(user.pk)), # id del usuario encriptado - convertimos el id del usuario a bytes y luego lo encriptamos
                'token': default_token_generator.make_token(user), # token de activación que se genera por cada usuario
            })
            to_email = email # correo del destinatario
             # Enviamos el correo de activación
            send_email = EmailMessage(body_email, message, to=[to_email]) # Asignamos el cuerpo, mensaje y destinatario al correo
            send_email.send()
            messages.success(request, "Cuenta creada exitosamente. Por favor, verifica tu correo electrónico para activar tu cuenta.")
            return redirect('auths:register') # Redirigimos a la misma página de registro   
    else:
        formulario=FormularioRegistro()
           
    context = {
        'formulario': formulario,
    }
   
    return render(request, 'auths/register.html', context)

def verify_account(request, uidb64, token):
    uid =urlsafe_base64_decode(uidb64).decode()
    user = models.Auth._default_manager.get(pk=uid)
    if user is not None and default_token_generator.check_token(user, token):
        user.is_active = True
        user.save()
        messages.success(request, "¡Gracias por activar tu cuenta! Ahora puedes iniciar sesión.")
        return redirect('auths:login')
    return HttpResponse("Verificación de cuenta")