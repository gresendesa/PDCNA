from django.contrib import admin
from .models import Participante, Levantamento, Levantamento_dados
# Register your models here.

admin.site.register(Participante)
admin.site.register(Levantamento)
admin.site.register(Levantamento_dados)