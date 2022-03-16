from django.db import models

# Create your models here.
class Categoria(models.Model):
    nome = models.CharField(
        max_length=60,
        unique=True,
    )

    def __str__(self) -> str:
        return f"{self.id} {self.nome}"


class Evento(models.Model):
    nome = models.CharField(
        max_length=100,
    )
    categoria = models.ForeignKey(
        Categoria,
        on_delete=models.SET_NULL,
        null=True,
    )
    local = models.CharField(
        max_length=60,
        blank=True,
    )
    link = models.CharField(
        max_length=256,
        blank=True,
    )
    data_evento = models.DateField(
        null=True,
    )
    participantes = models.IntegerField(default=0)
    def __str__(self) -> str:
        return f"{self.id} {self.nome}"

