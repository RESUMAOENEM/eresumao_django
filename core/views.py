from rest_framework.viewsets import ModelViewSet

from core.models import Resumo, Curtida, Favorito, Comentario
from core.serializers import (
    ResumoSerializer,
    CurtidaSerializer,
    FavoritoSerializer,
    ComentarioSerializer,
    ComentarioDetailSerializer,
)


class ResumoViewSet(ModelViewSet):
    queryset = Resumo.objects.all()
    serializer_class = ResumoSerializer


class CurtidaViewSet(ModelViewSet):
    queryset = Curtida.objects.all()
    serializer_class = CurtidaSerializer


class FavoritoViewSet(ModelViewSet):
    queryset = Favorito.objects.all()
    serializer_class = FavoritoSerializer


class ComentarioViewSet(ModelViewSet):
    queryset = Comentario.objects.all()

    def get_serializer_class(self):
        if self.action in ["list", "retrieve"]:
            return ComentarioDetailSerializer
        return ComentarioSerializer
