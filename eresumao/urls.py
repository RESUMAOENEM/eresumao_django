from django.contrib import admin
from django.urls import include, path

from rest_framework.routers import DefaultRouter

from core.views import ResumoViewSet, CurtidaViewSet, FavoritoViewSet, ComentarioViewSet

router = DefaultRouter()
router.register(r"resumos", ResumoViewSet)
router.register(r"curtidas", CurtidaViewSet)
router.register(r"favoritos", FavoritoViewSet)
router.register(r"comentarios", ComentarioViewSet)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include(router.urls)),
]
