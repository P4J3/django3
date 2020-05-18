from django.urls import reverse_lazy
from django.test import TestCase
from django.test import Client

class IndexViewTestCase(TestCase):

        def setUp(self):

            self.dados = {
                'nome': 'João Victor',
                'email': 'joao@gmail.com',
                'assunto': 'Assunto',
                'mensagem': 'Mensagem'
            }

            self.cliente = Client()


        def test_form_valid(self):
            request = self.client.post(reverse_lazy('index'), data=self.dados)
            self.assertEquals(request.status_code, 302)


        def test_form_invalid(self):
            request = self.cliente.post(reverse_lazy('index'), data={'nome':'Voão', 'assunto': 'Assunto'})
            self.assertEquals(request.status_code, 200)