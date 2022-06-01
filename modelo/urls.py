from django.urls import path,re_path
from django.contrib.auth.decorators import login_required
from .views import EliminarPaciente,EditarPaciente,CrearPaciente, buscar_autorizaciones1,buscar_paciente,CrearModalPaciente,ListarPacientes
from .views import Eliminarcardiologo,Editarcardiologo,Crearcardiologo,buscar_cardiologo,CrearModalcardiologo, buscar_autorizaciones
from .views import EditarPreQuirurgico, EliminarPreQuirurgico, CrearPreQuirurgico, CrearModalPreQuirurgico, buscar_PreQuirurgico




urlpatterns = [
    path('crear_paciente/', login_required(CrearPaciente.as_view()), name = 'crear_paciente'),
    path('crear__paciente/', login_required(CrearModalPaciente.as_view()), name = 'crear__paciente'),
    path('listar_paciente/', login_required(buscar_paciente), name = 'listar_paciente'),
    path('editar_paciente/<int:pk>', login_required(EditarPaciente.as_view()), name = 'editar_paciente'),
    path('eliminar_paciente/<int:pk>',login_required(EliminarPaciente.as_view()), name = 'eliminar_paciente'),

    path('crear_cardiologo/', login_required(Crearcardiologo.as_view()), name = 'crear_cardiologo'),
    path('crear__cardiologo/', login_required(CrearModalcardiologo.as_view()), name = 'crear__cardiologo'),
    path('listar_cardiologo/', login_required(buscar_cardiologo), name = 'listar_cardiologo'),
    path('editar_cardiologo/<int:pk>', login_required(Editarcardiologo.as_view()), name = 'editar_cardiologo'),
    path('eliminar_cardiologo/<int:pk>',login_required(Eliminarcardiologo.as_view()), name = 'eliminar_cardiologo'),
    
    path('crear_PreQuirurgico/', login_required(CrearPreQuirurgico.as_view()), name = 'crear_PreQuirurgico'),
    path('crear__PreQuirurgico/', login_required(CrearModalPreQuirurgico.as_view()), name = 'crear__PreQuirurgico'),
    path('listar_PreQuirurgico/', login_required(buscar_PreQuirurgico), name = 'listar_PreQuirurgico'),
    path('editar_PreQuirurgico/<int:pk>', login_required(EditarPreQuirurgico.as_view()), name = 'editar_PreQuirurgico'),
    path('eliminar_PreQuirurgico/<int:pk>',login_required(EliminarPreQuirurgico.as_view()), name = 'eliminar_PreQuirurgico'),

    path('listar_autorizaciones/', login_required(buscar_autorizaciones), name = 'listar_autorizaciones'),

    ]