from django.contrib.auth.models import User

from rest_framework.generics import CreateAPIView, UpdateAPIView
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ModelViewSet

from core.models import Comentario, Curtida, Favorito, Resumo
from core.serializers import (
    ComentarioDetailSerializer,
    ComentarioSerializer,
    CurtidaSerializer,
    FavoritoSerializer,
    RegisterSerializer,
    ResumoSerializer,
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


class RegisterView(CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer
