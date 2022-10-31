from rest_framework.serializers import ModelSerializer

from core.models import Resumo, Curtida, Favorito, Comentario


class ResumoSerializer(ModelSerializer):
    class Meta:
        model = Resumo
        fields = "__all__"


class CurtidaSerializer(ModelSerializer):
    class Meta:
        model = Curtida
        fields = "__all__"


class FavoritoSerializer(ModelSerializer):
    class Meta:
        model = Favorito
        fields = "__all__"


class ComentarioSerializer(ModelSerializer):
    class Meta:
        model = Comentario
        fields = "__all__"
