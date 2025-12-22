from django.db import models
from django.contrib.auth.models import User # Es el mas comun
from django.contrib.auth.models import AbstractUser, BaseUserManager, PermissionsMixin # Es mas complejo para personalizar el modelo de usuario

class UserManager(BaseUserManager):
    def create_user(self, username, name, lastname, email, password=None, **extra_fields):
        if not username:
            raise ValueError("El nombre de usuario debe ser proporcionado")
        if not name:
            raise ValueError("El nombre debe ser proporcionado")
        if not lastname:
            raise ValueError("El apellido debe ser proporcionado")
        if not email:
            raise ValueError("El email debe ser proporcionado")
        user = self.model(
            username=username, 
            name=name,  
            lastname=lastname, 
            email=self.normalize_email(email), 
            **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        print("Usuario creado:", user)
        return user

    def create_superuser(self, username, name, lastname, email, password=None, **extra_fields):
        extra_fields.setdefault('is_admin', True)
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superadmin", True)
        #extra_fields.setdefault('is_superuser', True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("El superusuario debe tener is_staff=True.")
        if extra_fields.get("is_superadmin") is not True:
            raise ValueError("El superusuario debe tener is_superadmin=True.")

        return self.create_user(username, name, lastname, email, password, **extra_fields)

class Auth(AbstractUser, PermissionsMixin):
    username = models.CharField(max_length=50, unique=True) # verificar si tiene que ser único ya que se genera segun el correo
    name = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    email = models.EmailField(max_length=150, unique=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)

    # required
    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    is_superadmin = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'name', 'lastname']

    objects = UserManager() # Esto sirve para la herencia cuandp instancies un usuario User podras usar los metodos de UserManager, ejemplo: usuario=User.object.create:user(….)

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None): # Este metodo es para verificar si el usuario tiene un permiso para realizar cualquier accion en el administrador
        return self.is_admin

    def has_module_perms(self, app_label): # Este metodo es para verificar si el usuario tiene permisos para acceder a cualquier modulo, asi cuando se loguee podra ingresar al carrito de compras, dashboard, pasarela de pago, etc
        return True