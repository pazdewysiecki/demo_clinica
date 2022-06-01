from email.policy import default
from inspect import signature
from tabnanny import verbose
from django.db import models
from django import forms
from jsignature.fields import JSignatureField
from jsignature.widgets import JSignatureWidget
from jsignature.mixins import JSignatureFieldsMixin
from usuarios.models import Usuario

#from ckeditor import RichTextField

class paciente (models.Model):
    id = models.AutoField(primary_key= True)
    fecha_creacion = models.DateField('fecha_creacion',auto_now=False , auto_now_add=True)
    nombre_paciente = models.CharField(max_length = 200, blank = False, default=None, verbose_name='nombre_paciente')
    dni_paciente =  models.CharField(max_length = 100, blank = True, default=None, verbose_name='dni_paciente')

    def __str__(self):
        return str(self.nombre_paciente)
         

    class Meta:
        ordering = ['nombre_paciente']
        verbose_name = 'paciente'
        verbose_name_plural = 'pacientes'



class cardiologo (models.Model):
    id = models.AutoField(primary_key= True)
    fecha_creacion = models.DateField('fecha_creacion',auto_now=False , auto_now_add=True)
    paciente = models.ForeignKey(paciente, on_delete = models.CASCADE, null=True)
    estado_cardiologo = models.BooleanField ('estado_cardiologo', default=True)

    def __str__(self):
        return str(self.id)
         

    class Meta:
        ordering = ['id']
        verbose_name = 'cardiologo'
        verbose_name_plural = 'cardiologos'

class PreQuirurgico (models.Model):
    id = models.AutoField(primary_key= True)
    fecha_creacion = models.DateField('fecha_creacion',auto_now=False , auto_now_add=True)
    paciente = models.ForeignKey(paciente, on_delete = models.CASCADE, null=True)
    estado_prequirurgico = models.BooleanField ('estado_prequirurgico', default=True)

    def __str__(self):
        return str(self.id)
         

    class Meta:
        ordering = ['id']
        verbose_name = 'PreQuirurgico'
        verbose_name_plural = 'PreQuirurgicos'

