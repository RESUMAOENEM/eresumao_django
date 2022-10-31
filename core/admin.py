from django.contrib import admin

from core.models import Comentario, Curtida, Favorito, Resumo


@admin.register(Resumo)
class ResumoAdmin(admin.ModelAdmin):
    list_display = ("titulo", "conteudo", "data")
    search_fields = ("titulo", "email")
    list_filter = ("titulo",)
    ordering = ("titulo", "data")


@admin.register(Curtida)
class CurtidaAdmin(admin.ModelAdmin):
    list_display = (
        "curtido_por",
        "resumo",
    )
    search_fields = (
        "curtido_por",
        "resumo",
    )
    list_filter = (
        "curtido_por",
        "resumo",
    )
    ordering = (
        "curtido_por",
        "resumo",
    )


@admin.register(Favorito)
class FavoritoAdmin(admin.ModelAdmin):
    list_display = (
        "favoritado_por",
        "resumo",
    )
    search_fields = (
        "favoritado_por",
        "resumo",
    )
    list_filter = (
        "favoritado_por",
        "resumo",
    )
    ordering = (
        "favoritado_por",
        "resumo",
    )


@admin.register(Comentario)
class ComentarioAdmin(admin.ModelAdmin):
    list_display = ("comentado_por", "texto", "data")
    search_fields = ("comentado_por", "data")
    list_filter = ("comentado_por", "data")
    ordering = ("comentado_por", "data")
    list_per_page = 25
