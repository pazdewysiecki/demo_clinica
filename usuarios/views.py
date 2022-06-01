import json
import os
from pprint import pprint 
from django.shortcuts import redirect
from django.http import HttpResponseRedirect, HttpResponse, HttpRequest
from django.shortcuts import render, HttpResponse
from django.urls import reverse_lazy
from django.core.serializers import serialize
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect
from django.views.generic import View
from django.views.generic.edit import FormView
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth import login, logout
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, TemplateView
from usuarios.mixins import LoginYSuperUsuarioMixin, ValidarPermisosRequeridosMixin
from usuarios.models import Usuario
from usuarios.forms import CambiarPasswordForm
from django.http import JsonResponse
from django.utils.translation import gettext_lazy as _
from django.conf.urls import handler404
from .forms import FormularioLogin, FormularioUsuario
from django.core import serializers
from django.core.paginator import Paginator
#from tramites.models import Clientes_Tramites
#from .forms import FormularioLogin, FormularioUsuario


# Create your views here.



class Login(LoginView):
    template_name = 'login.html'
    form_class = FormularioLogin
    success_url = reverse_lazy ('login')
    
    @method_decorator(csrf_protect)
    @method_decorator(never_cache)
    def dispatch(self,request, *args, **kwargs):
        if request.user.is_authenticated:
            return HttpResponseRedirect(self.get_success_url())
        else:
            return super(Login,self).dispatch(request,*args,**kwargs)
    def form_valid(self,form):
        login(self.request,form.get_user())
        return super(Login,self).form_valid(form)

def logoutUsuario(request):
    logout(request)
    return HttpResponseRedirect('/accounts/login/')

def is_ajax(request):
        return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'

class InicioUsuarios(ValidarPermisosRequeridosMixin, TemplateView):
    template_name='usuarios/listar_usuarios.html'

class ListadoUsuario(ValidarPermisosRequeridosMixin,ListView):
    model = Usuario
    template_name = 'usuarios/listar_usuarios.html'
    permission_required = ('usuarios.view_usuario','usuarios.add_usuario','usuarios.delete_usuario','usuarios.change_usuario')
    context_object_name = 'usuarios'
    queryset = Usuario.objects.all()

class ListadoUsuario2(ListView):
    model = Usuario
    #template_name = 'usuarios/inicio_usuarios.html'

    def get_queryset(self):
        return self.model.objects.filter(is_active=True)

    """
    def get(self,request,*args,**kwargs):
            if is_ajax(request=request): 
                pprint(self.kwargs)
                return HttpResponse(serialize('json', self.get_queryset()), 'application/json')
            else:
                return redirect ('usuarios:inicio_usuarios')
    """
    """
    def get(self,request,*args,**kwargs):
            if is_ajax(request=request):
                lista_usuarioss = []
                for usuario in self.get_queryset():
                    data_usuario = {}
                    data_usuario['id']= usuario.id
                    data_usuario['nombre']= usuario.nombre
                    data_usuario['username']= usuario.username 
                    lista_usuarioss.append(data_usuario)
                lista_usuarios = json.dumps(lista_usuarioss)
                pprint(lista_usuarios)
                return HttpResponse(lista_usuarios,'application/json')
            else:
                return render (request, self.template_name)
    """
    def get(self, request, *args, **kwargs):
            if is_ajax(request=request):
                data_json = serializers.serialize('json',self.get_queryset())
                pprint(data_json)
                return HttpResponse(data_json, content_type='application/json')
            else:
                return render(request, self.template_name)
     




   # succes_url = reverse_lazy/('usuarios:listar_usuarios')

class RegistrarUsuario(ValidarPermisosRequeridosMixin,CreateView):
    model = Usuario
    form_class = FormularioUsuario
    template_name = 'usuarios/crear_usuario.html'
    permission_required = ('usuarios.view_usuario','usuarios.add_usuario','usuarios.delete_usuario','usuarios.change_usuario')
    #success_url = reverse_lazy ('usuarios:listar_usuarios')
    
    def post(self,request,*args,**kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            nuevo_usuario = Usuario(
                username = form.cleaned_data.get('username'),
                nombre = form.cleaned_data.get('nombre')
                )
            nuevo_usuario.set_password(form.cleaned_data.get('password1'))
            nuevo_usuario.save()
            return redirect('usuarios:listar_usuarios')
        else:
            return render(request,self.template_name,{'form':form})

class ModalRegistrarUsuario(ValidarPermisosRequeridosMixin,CreateView):
    model = Usuario
    template_name = 'usuarios/crear__usuario.html'
    permission_required = ('usuarios.view_usuario','usuarios.add_usuario','usuarios.delete_usuario','usuarios.change_usuario')
    form_class = FormularioUsuario
    success_url = reverse_lazy ('usuarios:listar_usuarios')

class EditarUsuario(ValidarPermisosRequeridosMixin,UpdateView):
    model = Usuario
    template_name = 'usuarios/editar_usuarios.html'
    permission_required = ('usuarios.view_usuario','usuarios.add_usuario','usuarios.delete_usuario','usuarios.change_usuario')
    form_class = FormularioUsuario
    success_url = reverse_lazy ('usuarios:listar_usuarios')

class EliminarUsuario(ValidarPermisosRequeridosMixin,DeleteView):
    model = Usuario
    permission_required = ('usuarios.view_usuario','usuarios.add_usuario','usuarios.delete_usuario','usuarios.change_usuario')
    success_url = reverse_lazy ('usuarios:listar_usuarios')
         
class CambiarPassword(View):
    template_name = 'usuarios/cambiar_password.html'
    form_class = CambiarPasswordForm
    success_url= reverse_lazy ('home')

    def get(self,request,*args,**kwargs):
        return render(request,self.template_name, {'form': self.form_class})

    def post(self,request,*args,**kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = Usuario.objects.filter(id=request.user.id)
            if user.exists():
                user =user.first()
                user.set_password(form.cleaned_data.get('password1'))
                user.save()
                return redirect(self.success_url)
            return redirect (self.success_url)
        else:
            form = self.form_class(request.POST)
            return render(request,self.template_name, {'form': form})

