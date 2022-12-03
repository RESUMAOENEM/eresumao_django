from django.contrib.auth.models import Group
from rest_framework.serializers import ModelSerializer

from dj_rest_auth.registration.serializers import RegisterSerializer
from dj_rest_auth.serializers import UserDetailsSerializer


from core.models import Comentario, Curtida, Favorito, Resumo


class UsuarioNestedSerializer(UserDetailsSerializer):
    class Meta(UserDetailsSerializer.Meta):
        fields = ["pk", "username", "first_name", "last_name"]


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
    comentado_por = UsuarioNestedSerializer()

    class Meta:
        model = Comentario
        fields = "__all__"
        depth = 1


class CustomRegisterSerializer(RegisterSerializer):
    def save(self, request):
        user = super().save(request)
        user.groups.add(Group.objects.get(name="estudante"))
        return user


class CustomUserDetailsSerializer(UserDetailsSerializer):
    class Meta(UserDetailsSerializer.Meta):
        fields = UserDetailsSerializer.Meta.fields + ("is_active", "is_staff", "groups")
