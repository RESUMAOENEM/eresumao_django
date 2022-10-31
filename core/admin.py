from django.contrib import admin

from core.models import Resumo, Curtida, Favorito, Comentario

admin.site.register(Resumo)
admin.site.register(Curtida)
admin.site.register(Favorito)
admin.site.register(Comentario)
