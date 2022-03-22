from django.test import TestCase, Client
from agenda.models import Evento, Categoria
from datetime import date
# Create your tests here.

class TestPaginaInicial(TestCase):
    def test_lista_eventos(self):
        cliente = Client()
        response = cliente.get("/")
        self.assertContains(response, "<th>Nome</th>")
        self.assertContains(response, "<th>Data</th>")
        self.assertTemplateUsed(response, "agenda/lista_eventos.html")

class TestListagemEventos(TestCase):
    def setUp(self) -> None:
        categoria = Categoria()
        categoria.nome = "Backend"
        categoria.save()

        self.evento = Evento()
        self.evento.nome = "Aula de Python"
        self.evento.categoria = categoria
        self.evento.local = "Rio Grande do Sul"
        self.evento.data_evento = date.today()
        self.evento.save()

    def test_evento_hoje(self):
        cliente = Client()
        response = cliente.get("/")
        self.assertContains(response, "Aula de Python")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context["eventos"][0], self.evento)
        self.assertIn(self.evento, list(response.context["eventos"]))

class TestListagemEventosSemData(TestCase):
    def setUp(self) -> None:
        categoria = Categoria()
        categoria.nome = "Backend"
        categoria.save()

        self.evento = Evento()
        self.evento.nome = "Aula de Python"
        self.evento.categoria = categoria
        self.evento.local = "Rio Grande do Sul"
        self.evento.data_evento = None
        self.evento.save()

    def test_evento_sem_data(self):
        cliente = Client()
        response = cliente.get("/")
        self.assertContains(response, "Aula de Python")
        self.assertContains(response, "A definir")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context["eventos"][0], self.evento)
        self.assertIn(self.evento, list(response.context["eventos"]))
