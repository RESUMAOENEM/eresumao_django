from django.contrib import admin
from django.urls import include, path

from rest_framework.routers import DefaultRouter

from core.views import ResumoViewSet, CurtidaViewSet, FavoritoViewSet, ComentarioViewSet

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

router = DefaultRouter()
router.register(r"resumos", ResumoViewSet)
router.register(r"curtidas", CurtidaViewSet)
router.register(r"favoritos", FavoritoViewSet)
router.register(r"comentarios", ComentarioViewSet)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include(router.urls)),
    path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]
