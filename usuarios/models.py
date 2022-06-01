from cgi import MiniFieldStorage
from email.mime.image import MIMEImage
from enum import unique
import mimetypes
from unittest.util import _MAX_LENGTH
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.forms import BooleanField, ImageField

# Create your models here.

class UsuarioManager(BaseUserManager):
    def _create_user(self,username,nombre,especialidad,password,is_staff,is_superuser,**extra_fields):
        user = self.model(
            username = username,
            nombre = nombre,
            especialidad = especialidad,
            is_staff = is_staff,
            is_superuser = is_superuser,
            **extra_fields 
        )
        user.set_password(password)
        user.save(using=self.db)
        return user
        
    def create_user(self,username,nombre,especialidad,password = None, **extra_fields):
        return self._create_user(username,nombre,especialidad,password,False,False,**extra_fields)  

    def create_superuser(self,username,nombre,especialidad,password = None, **extra_fields):
        return self._create_user(username,nombre,especialidad,password,True,True,**extra_fields)



class Usuario(AbstractBaseUser, PermissionsMixin):
    id = models.AutoField(primary_key= True)
    username = models.CharField('Username/Mail', unique=True, max_length=100)
    nombre = models.CharField(max_length = 200, blank = False, default=None, verbose_name='nombre')
    especialidad = models.CharField(max_length = 100, blank = True, default=None, verbose_name='especialidad')
    is_active = models.BooleanField(default=True) #usuarios que inician sesión
    is_staff = models.BooleanField(default=False) #usuario en el administrador de django
    objects = UsuarioManager()
    """
        imagen = models.ImageField('Imgen de Perfil', upload_to='perfil/', height_field=None, width_field=None, max_length=200, blank= True, null = True)
    """

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['nombre','especialidad']

    class Meta:
        permissions = [('permiso_desde_codigo', 'Este es un permiso creado desde código'),
                        ('segundo_permiso_codigo', 'Este es un segundo permiso creado desde código')] 

    def __str__(self):
        return f'{self.nombre}'