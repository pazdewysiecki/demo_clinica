from dataclasses import field, fields
import imp
from django import forms
from django.conf import Settings
from .models import cardiologo, paciente, PreQuirurgico



class pacienteForm(forms.ModelForm):
    class Meta:
        model = paciente
        fields = ['nombre_paciente', 'dni_paciente', 'id' ]
        labels = {
                'nombre_paciente': "Nombre del paciente:",
                'dni_paciente': "Número de DNI:",
                'id': "Código del paciente:",
            }
        widgets = {
            'nombre_paciente': forms.TextInput(
                attrs = {
                    'class':'form-control',
                    'placeholder':'Ingrese el nombre del paciente',
                    'id':'nombre_paciente'
                }
            ),
            'dni_paciente': forms.TextInput (
                 attrs = {
                    'class':'form-control',
                    'placeholder':'Ingrese el DNI del paciente:',
                    'id':'dni_paciente'
                }
            )
        }

class cardiologoForm(forms.ModelForm):

    class Meta:
        model = cardiologo
        fields = ['paciente', 'estado_cardiologo', 'id']
        labels = {
                'paciente': "Código de paciente:",
                'estado_cardiologo': "Estado Cardiología:",
            }
        widgets = {
            'paciente': forms.TextInput (
                 attrs = {
                    'class':'form-control',
                    'placeholder':'Ingrese el código del paciente:',
                    'id':'paciente'
                }
            ),   
        }

class PreQuirurgicoForm(forms.ModelForm):
    class Meta:
        model = PreQuirurgico
        fields = ['paciente', 'estado_prequirurgico', 'id']
        labels = {
                'paciente': "Código de paciente:",
                'estado_prequirurgico': "Estado PreQuirurgico:",
            }
        widgets = {
            'paciente': forms.TextInput (
                 attrs = {
                    'class':'form-control',
                    'placeholder':'Ingrese el código del paciente:',
                    'id':'paciente'
                }
            )
        }

