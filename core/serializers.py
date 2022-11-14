from django.contrib.auth.models import Group
from rest_framework.serializers import ModelSerializer

from djoser.serializers import (
    UserCreateSerializer as BaseUserRegistrationSerializer,
    UserSerializer,
)

from core.models import Comentario, Curtida, Favorito, Resumo


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


class ComentarioDetailSerializer(ModelSerializer):
    class Meta:
        model = Comentario
        fields = "__all__"
        depth = 1


class CustomUserRegistrationSerializer(BaseUserRegistrationSerializer):
    class Meta(BaseUserRegistrationSerializer.Meta):
        fields = (
            "id",
            "email",
            "username",
            # "first_name",
            # "last_name",
            "password",
        )

    def perform_create(self, validated_data):
        user = super().perform_create(validated_data)
        user.groups.add(Group.objects.get(name="estudante"))
        return user


class CustomUserSerializer(UserSerializer):
    class Meta(UserSerializer.Meta):
        fields = ("id", "username", "email", "first_name", "last_name", "is_staff")
