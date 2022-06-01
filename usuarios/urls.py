from pipes import Template
from django.urls import path
from usuarios.views import ListadoUsuario, RegistrarUsuario,ModalRegistrarUsuario, EditarUsuario, EliminarUsuario, CambiarPassword
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from usuarios.views import InicioUsuarios

urlpatterns = [
    path('inicio_usuarios/', InicioUsuarios.as_view(), name='inicio_usuarios'),
    path('listar_usuarios/', login_required(ListadoUsuario.as_view()), name='listar_usuarios'),
    path('editar_usuarios/<int:pk>', login_required(EditarUsuario.as_view()), name='editar_usuarios'),
    path('eliminar_usuarios/<int:pk>', login_required(EliminarUsuario.as_view()), name='eliminar_usuarios'),
    path('registrar_usuarios/', login_required(RegistrarUsuario.as_view()), name='registrar_usuarios'),
    path('registrar__usuarios/', login_required(ModalRegistrarUsuario.as_view()), name='registrar__usuarios'),
    path('cambiar_password/', login_required(CambiarPassword.as_view()), name='cambiar_password'),
]



