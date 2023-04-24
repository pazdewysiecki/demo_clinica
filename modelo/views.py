from django.shortcuts import render
from ast import Try
from http import client
from multiprocessing import context
from pydoc import cli
from django.shortcuts import redirect, render
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import TemplateView,ListView, UpdateView, CreateView, DeleteView
from django.views import generic
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy 
from django.http import HttpResponse
from requests import request
from .forms import cardiologoForm, pacienteForm, PreQuirurgicoForm
from .models import cardiologo, paciente, PreQuirurgico
from django.core.paginator import Paginator
from django.conf import settings
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.contrib.staticfiles import finders
from django.core.exceptions import ValidationError
from django import forms
from usuarios.models import Usuario
from django.contrib.auth.decorators import permission_required
from usuarios.mixins import ValidarPermisosRequeridosMixin
# Create your views here.


#Clase para inciar#

class Inicio(TemplateView):
    template_name = 'login.html'

class InicioSistema(TemplateView):
    template_name = 'home.html'

class Meta:
        ordering = ('date',)


#Clase para Pacientes

@permission_required('modelo.view_paciente',login_url='home')
def buscar_paciente(request):
        busqueda = request.GET.get("buscar")
        pacientes = paciente.objects.all().order_by('-id')
        paginator = Paginator(pacientes, 50)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        if busqueda:
            pacientes = paciente.objects.filter(
                Q (nombre_paciente__icontains = busqueda) |
                Q (dni_paciente__icontains = busqueda) |
                Q (id__icontains = busqueda)
            ).distinct()
            return render(request, 'modelo/listar_paciente.html', {'pacientes':pacientes})
        else:
            return render(request, 'modelo/listar_paciente.html', {'pacientes': page_obj})


class EditarPaciente(ValidarPermisosRequeridosMixin,UpdateView):
    model = paciente
    template_name = 'modelo/modalpaciente.html'
    permission_required = ('modelo.view_paciente','modelo.add_paciente','modelo.delete_paciente','modelo.change_paciente')
    form_class = pacienteForm
    success_url = reverse_lazy ('modelo:listar_paciente')

class CrearPaciente(ValidarPermisosRequeridosMixin,CreateView):
    model = paciente
    form_class = pacienteForm
    template_name = 'modelo/crear_paciente.html'
    permission_required = ('modelo.view_paciente','modelo.add_paciente','modelo.delete_paciente','modelo.change_paciente')
    success_url = reverse_lazy ('modelo:listar_paciente')

class CrearModalPaciente(ValidarPermisosRequeridosMixin,CreateView):
    model = paciente
    template_name = 'modelo/modalcrearpaciente.html'
    permission_required = ('modelo.view_paciente','modelo.add_paciente','modelo.delete_paciente','modelo.change_paciente')
    form_class = pacienteForm
    success_url = reverse_lazy ('modelo:listar_paciente')

class EliminarPaciente(ValidarPermisosRequeridosMixin,DeleteView):
    model = paciente
    permission_required = ('modelo.view_paciente','modelo.add_paciente','modelo.delete_paciente','modelo.change_paciente')
    success_url = reverse_lazy ('modelo:listar_paciente')

#Clase para Cardiologo

@permission_required('modelo.view_cardiologo',login_url='home')
@permission_required('modelo.add_cardiologo',login_url='home')
@permission_required('modelo.delete_cardiologo',login_url='home')
@permission_required('modelo.change_cardiologo',login_url='home')
def buscar_cardiologo(request):
        busqueda = request.GET.get("buscar")
        cardiologos = cardiologo.objects.all().order_by('-id')
        paginator = Paginator(cardiologos, 50)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        if busqueda:
            cardiologos = cardiologo.objects.filter(
                Q (paciente__nombre_paciente__icontains = busqueda) |
                Q (id__icontains = busqueda)
            ).distinct()
            return render(request, 'modelo/listar_cardiologo.html', {'cardiologos':cardiologos})
        else:
            return render(request, 'modelo/listar_cardiologo.html', {'cardiologos': page_obj})


class Editarcardiologo(ValidarPermisosRequeridosMixin,UpdateView):
    model = cardiologo
    template_name = 'modelo/modalcardiologo.html'
    permission_required = ('modelo.view_cardiologo','modelo.add_cardiologo','modelo.delete_cardiologo','modelo.change_cardiologo')
    form_class = cardiologoForm
    success_url = reverse_lazy ('modelo:listar_cardiologo')

class Crearcardiologo(ValidarPermisosRequeridosMixin,CreateView):
    model = cardiologo
    form_class = cardiologoForm
    template_name = 'modelo/crear_cardiologo.html'
    permission_required = ('modelo.view_cardiologo','modelo.add_cardiologo','modelo.delete_cardiologo','modelo.change_cardiologo')
    success_url = reverse_lazy ('modelo:listar_cardiologo')

class CrearModalcardiologo(ValidarPermisosRequeridosMixin,CreateView):
    model = cardiologo
    template_name = 'modelo/modalcrearcardiologo.html'
    permission_required = ('modelo.view_cardiologo','modelo.add_cardiologo','modelo.delete_cardiologo','modelo.change_cardiologo')
    form_class = cardiologoForm
    success_url = reverse_lazy ('modelo:listar_cardiologo')

class Eliminarcardiologo(ValidarPermisosRequeridosMixin,DeleteView):
    model = cardiologo
    permission_required = ('modelo.view_cardiologo','modelo.add_cardiologo','modelo.delete_cardiologo','modelo.change_cardiologo')
    success_url = reverse_lazy ('modelo:listar_cardiologo')



#Clase para Prequirurgico

@permission_required('modelo.view_prequirurgico',login_url='home')
@permission_required('modelo.add_prequirurgico',login_url='home')
@permission_required('modelo.delete_prequirurgico',login_url='home')
@permission_required('modelo.change_prequirurgico',login_url='home')
def buscar_PreQuirurgico(request):
        busqueda = request.GET.get("buscar")
        PreQuirurgicos = PreQuirurgico.objects.all().order_by('-id')
        paginator = Paginator(PreQuirurgicos, 50)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        if busqueda:
            PreQuirurgicos = PreQuirurgico.objects.filter(
                Q (paciente__icontains = busqueda) |
                Q (nombre_paciente__icontains = busqueda) |
                Q (id__icontains = busqueda)
            ).distinct()
            
            return render(request, 'modelo/listar_PreQuirurgico.html', {'PreQuirurgicos':PreQuirurgicos})
        else:
            return render(request, 'modelo/listar_PreQuirurgico.html', {'PreQuirurgicos': page_obj})


class EditarPreQuirurgico(ValidarPermisosRequeridosMixin,UpdateView):
    model = PreQuirurgico
    template_name = 'modelo/modalPreQuirurgico.html'
    permission_required = ('modelo.view_prequirurgico','modelo.add_prequirurgico','modelo.delete_prequirurgico','modelo.change_prequirurgico')
    form_class = PreQuirurgicoForm
    success_url = reverse_lazy ('modelo:listar_PreQuirurgico')

class CrearPreQuirurgico(ValidarPermisosRequeridosMixin,CreateView):
    model = PreQuirurgico
    form_class = PreQuirurgicoForm
    template_name = 'modelo/crear_PreQuirurgico.html'
    permission_required = ('modelo.view_prequirurgico','modelo.add_prequirurgico','modelo.delete_prequirurgico','modelo.change_prequirurgico')
    success_url = reverse_lazy ('modelo:listar_PreQuirurgico')

class CrearModalPreQuirurgico(ValidarPermisosRequeridosMixin,CreateView):
    model = PreQuirurgico
    template_name = 'modelo/modalcrearPreQuirurgico.html'
    permission_required = ('modelo.view_prequirurgico','modelo.add_prequirurgico','modelo.delete_prequirurgico','modelo.change_prequirurgico')
    form_class = PreQuirurgicoForm
    success_url = reverse_lazy ('modelo:listar_PreQuirurgico')

class EliminarPreQuirurgico(ValidarPermisosRequeridosMixin,DeleteView):
    model = PreQuirurgico
    permission_required = ('modelo.view_prequirurgico','modelo.add_prequirurgico','modelo.delete_prequirurgico','modelo.change_prequirurgico')
    success_url = reverse_lazy ('modelo:listar_PreQuirurgico')

#Listado autorizaciones

def buscar_autorizaciones1(request):
        pacientes = paciente.objects.all()
        cardiologos = cardiologo.objects.all()
        PreQuirurgicos = PreQuirurgico.objects.all()
    
        return render(request, 'modelo/listar_autorizaciones.html', {'pacientes':pacientes,'cardiologos':cardiologos, 'PreQuirurgicos':PreQuirurgicos})

def buscar_autorizaciones2(request):
        busqueda = request.GET.get("buscar")
        resultado = []
        pacientes = paciente.objects.all()
        cardiologos = cardiologo.objects.all().order_by('-id')
        PreQuirurgicos = PreQuirurgico.objects.all()
        paginator = Paginator(cardiologos, 50)
        paginator2 = Paginator(PreQuirurgicos, 50)
        page_number = request.GET.get('page')
        page_obj = paginator2.get_page(page_number)
        page_number2 = request.GET.get('page2')
        page_obj2 = paginator.get_page(page_number2)
        resultado.append(PreQuirurgicos)
        resultado.append(cardiologos)
        resultado.append(pacientes)

        if busqueda:
                pacientes = paciente.objects.filter(
                    Q (dni_paciente__icontains = busqueda) |
                    Q (nombre_paciente__icontains= busqueda) 
                ).distinct()
                return render(request, 'modelo/listar_autorizaciones.html', {'pacientes':pacientes,'cardiologos':cardiologos, 'PreQuirurgicos':PreQuirurgicos})
        else:
            return render(request, 'modelo/listar_autorizaciones.html', {'pacientes':pacientes,'cardiologos':cardiologos, 'PreQuirurgicos':PreQuirurgicos})

class ListarPacientes1(ListView):
    model = paciente, cardiologo
    template_name = 'modelo/listar_autorizaciones.html'
    resultado = []
    resultado.append(PreQuirurgico)
    resultado.append(cardiologo)
    resultado.append(paciente)
    queryset = paciente.objects.all()
    queryset = cardiologo.objects.all()


class ListarPacientes2(generic.ListView):
    template_name = 'modelo/listar_autorizaciones.html'
    context_object_name = 'pacientes'

    def get_queryset(self):
        return paciente.objects.order_by('id')

    def get_context_data(self, **kwargs):
        context = super(ListarPacientes, self).get_context_data(**kwargs)
        context['cardiologos'] = cardiologo.objects.all()
        return context

class ListarPacientes(ListView):
    model = paciente, cardiologo
    template_name = 'modelo/listar_autorizaciones.html'
    context_object_name = 'pacientes'
    queryset = paciente.objects.all()

    def get_context_data(self, **kwargs):
        context = super(ListarPacientes, self).get_context_data(**kwargs)
        id = self.kwargs.get('id')
        context['cardiologos'] = cardiologo.objects.get(paciente=id)  
        return context


def buscar_autorizaciones3(request):
    cardiolog = cardiologo.objects.all()
    prequirurgico = PreQuirurgico.objects.filter()
    contexto = {'cardiologos':cardiolog, 'prequirurgicos':prequirurgico}
    return render (request,'modelo/listar_autorizaciones.html', contexto)

def buscar_autorizaciones(request):
        busqueda = request.GET.get("buscar")
        cardiologos = cardiologo.objects.all().order_by('-id')
        PreQuirurgicos = PreQuirurgico.objects.all().order_by('-id')
        paginator = Paginator(PreQuirurgicos, 1)
        paginator2 = Paginator(cardiologos, 1)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        page_obj2 = paginator2.get_page(page_number)

        if busqueda:
            PreQuirurgicos = PreQuirurgico.objects.filter(
                Q (paciente__id__icontains = busqueda) |
                Q (paciente__dni_paciente__icontains = busqueda) |
                Q (paciente__nombre_paciente__icontains = busqueda)
            ).distinct()
            cardiologos = cardiologo.objects.filter(
                Q (paciente__id__icontains = busqueda) |
                Q (paciente__dni_paciente__icontains = busqueda) |
                Q (paciente__nombre_paciente__icontains = busqueda)
            ).distinct() 
            return render(request, 'modelo/listar_autorizaciones.html', {'PreQuirurgicos': PreQuirurgicos, 'cardiologos': cardiologos})
        else:
            return render(request, 'modelo/listar_autorizaciones.html', {'PreQuirurgicos': page_obj,'cardiologos': page_obj2})
