from datetime import date
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from agenda.models import Categoria, Evento
from django.urls import reverse
from django.db.models import F

# Create your views here.
def acesso_raiz(request):
    eventos_nulos = Evento.objects.filter(data_evento__isnull=True)
    eventos = Evento.objects.filter(data_evento__gte=date.today())
    eventos = eventos | eventos_nulos
    eventos = eventos.order_by(F("data_evento").asc(nulls_last=True))
    return render(
        request=request,
        context={"eventos": eventos},
        template_name="agenda/lista_eventos.html",
    )

def exibir_evento(request, id):
    evento = get_object_or_404(Evento, id=id)
    # evento = Evento.objects.get(id=id)
    return render(
        request=request,
        context={"evento": evento},
        template_name="agenda/exibir_evento.html",
    )

def participar_evento(request):
    evento_id = request.POST.get("evento_id")
    evento = get_object_or_404(Evento, id=evento_id)
    evento.participantes += 1
    evento.save()
    return HttpResponseRedirect(
        reverse("exibir_evento", args=(evento_id,)),
    )

def listar_categorias(request):
    categorias = Categoria.objects.all()
    return render(
        request=request,
        context={"categorias": categorias},
        template_name="agenda/lista_categorias.html",
    )

def exibir_categoria(request, id):
    categoria = get_object_or_404(Categoria, id=id)
    qtd = Evento.objects.filter(categoria=categoria).count()
    return render(
        request=request,
        context={"categoria": categoria, "qtd": qtd},
        template_name="agenda/exibir_categoria.html",
    )
