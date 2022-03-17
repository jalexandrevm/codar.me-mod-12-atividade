from django.db import models

# Create your models here.
class Categoria(models.Model):
    nome = models.CharField(
        max_length=60,
        unique=True,
    )
    @classmethod
    def cria_categoria(cls, nome):
        if nome and nome != "":
            cat = Categoria(nome=nome)
            cat.save()
            return cat
        else:
            raise ValueError("Precisa ter um nome válido.")
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
    @classmethod
    def cria_evento(cls, nome, categ, local, link, data):
        if ((local and not link) or (not local and link)):
            ev = Evento(nome=nome, categoria=categ, local=local, link=link, data_evento=data)
            ev.save()
            return ev
        else:
            raise ValueError("Evento não pode possuir local e link.")

