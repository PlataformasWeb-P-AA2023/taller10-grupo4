from django.contrib import admin
from .models import Parroquia,Barrio
# Register your models here.

class ParroquiaAdmin(admin.ModelAdmin):
    list_display = ('nombre',"tipo")
    search_fields = ("nombre", "tipo")


class BarrioAdmin(admin.ModelAdmin):
    list_display = ('nombre',"numero_viviendas","numero_parques", "numero_edificios", "parroquia")
    search_fields = ("nombre","numero_viviendas","numero_parques", "numero_edificios", "parroquia")
     

admin.site.register(Parroquia, ParroquiaAdmin)
admin.site.register(Barrio, BarrioAdmin)