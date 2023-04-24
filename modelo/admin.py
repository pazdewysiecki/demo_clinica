from django.contrib import admin
from .models import *
#from import_export import resources
#from import_export.admin import ImportExportModelAdmin
# Register your models here.




#class ClientesResource(resources.ModelResource):
 #   class Meta:
  #      model = Clientes



class pacienteAdmin(admin.ModelAdmin):
    search_fields = ['nombre_paciente']
    list_display = ('nombre_paciente','dni_paciente')
    #resource_class = ClientesResource


class cardiologoAdmin(admin.ModelAdmin):
    search_fields = ['id']
    list_display = ('id','paciente','estado_cardiologo','fecha_creacion')

class PreQuirurgicoAdmin(admin.ModelAdmin):
    search_fields = ['id']
    list_display = ('id','paciente','estado_prequirurgico','fecha_creacion')






admin.site.register(paciente)
admin.site.register(PreQuirurgico)
admin.site.register(cardiologo)

#admin.site.register (Post)
