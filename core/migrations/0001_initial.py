# Generated by Django 4.1.2 on 2022-11-01 01:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Resumo",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("titulo", models.CharField(max_length=50)),
                ("conteudo", models.CharField(max_length=150)),
                ("data", models.DateTimeField(auto_now_add=True)),
                ("atualizado", models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name="Favorito",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "favoritado_por",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="favoritos",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "resumo",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="favoritos",
                        to="core.resumo",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Curtida",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "curtido_por",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="curtidas",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "resumo",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="curtidas",
                        to="core.resumo",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Comentario",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("texto", models.CharField(max_length=150)),
                ("data", models.DateTimeField(auto_now_add=True)),
                ("atualizado", models.DateTimeField(auto_now=True)),
                (
                    "comentado_por",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="comentarios",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "resumo",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="comentarios",
                        to="core.resumo",
                    ),
                ),
            ],
        ),
    ]
