from django.contrib import admin
from .models import Registro


class RegistroAdmin(admin.ModelAdmin):
    exclude = ('fecha_ingreso',)
    list_display = ('empresa', 'insumo_instalado', 'vence')
# Register your models here.
admin.site.register(Registro, RegistroAdmin)