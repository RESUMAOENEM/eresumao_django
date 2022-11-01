from django.contrib.auth.models import User

from django.contrib.auth.models import Group
from django.contrib.auth.password_validation import validate_password

from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from rest_framework.validators import UniqueValidator
from rest_framework_simplejwt.tokens import RefreshToken

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


class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True, validators=[UniqueValidator(queryset=User.objects.all())]
    )

    password = serializers.CharField(
        write_only=True, required=True, validators=[validate_password]
    )
    password2 = serializers.CharField(write_only=True, required=True)
    tokens = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = (
            "username",
            "password",
            "password2",
            "email",
            "first_name",
            "last_name",
            "tokens",
        )
        extra_kwargs = {
            "first_name": {"required": True},
            "last_name": {"required": True},
        }

    def get_tokens(self, user):
        tokens = RefreshToken.for_user(user)
        refresh = str(tokens)
        access = str(tokens.access_token)
        data = {"refresh": refresh, "access": access}
        return data

    def validate(self, attrs):
        if attrs["password"] != attrs["password2"]:
            raise serializers.ValidationError(
                {"password": "Password fields didn't match."}
            )

        return attrs

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data["username"],
            email=validated_data["email"],
            first_name=validated_data["first_name"],
            last_name=validated_data["last_name"],
        )

        user.set_password(validated_data["password"])
        user.groups.add(Group.objects.get(name="estudante"))
        user.save()

        return user
