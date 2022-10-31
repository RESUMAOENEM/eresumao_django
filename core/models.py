from django.contrib.auth.models import User
from django.db import models


class Resumo(models.Model):
    titulo = models.CharField(max_length=50)
    conteudo = models.CharField(max_length=150)
    data = models.DateTimeField(auto_now_add=True)
    atualizado = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.titulo


class Curtida(models.Model):
    curtido_por = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="curtidas"
    )
    resumo = models.ForeignKey(
        Resumo, on_delete=models.CASCADE, related_name="curtidas"
    )

    def __str__(self):
        return f"{self.curtido_por} curtiu o resumo '{self.resumo}'"


class Favorito(models.Model):
    favoritado_por = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="favoritos"
    )
    resumo = models.ForeignKey(
        Resumo, on_delete=models.CASCADE, related_name="favoritos"
    )

    def __str__(self):
        return f"{self.curtido_por} adicionou aos favoritos o resumo '{self.resumo}'"


class Comentario(models.Model):
    texto = models.CharField(max_length=150)
    data = models.DateTimeField(auto_now_add=True)
    atualizado = models.DateTimeField(auto_now=True)
    comentado_por = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="comentarios"
    )
    resumo = models.ForeignKey(
        Resumo, on_delete=models.CASCADE, related_name="comentarios"
    )

    def __str__(self):
        return f"{self.comentado_por} cometou: {self.texto}"
