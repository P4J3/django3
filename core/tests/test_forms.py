from django.test import TestCase
from core.forms import ContatoForm


class ContatoFormTestCase(TestCase):

    def setUp(self):
        #Simulando a criação de um formulário
        self.nome = 'João Victor'
        self.email = 'joaovictor@gmail.com'
        self.assunto = 'Algo'
        self.mensagem = 'Mensagem'


        self.dados = {
            'nome': self.nome,
            'email': self.email,
            'assunto': self.assunto,
            'mensagem': self.mensagem
        }

        #Passa os dados de self.dados como parâmetro para o Formulário. Que pega as chaves no dicinoário
        #e cria variáveis com ela
        self.form = ContatoForm(data=self.dados)

    def test_send_mail(self):
        form1 = ContatoForm(data=self.dados)
        form1.is_valid()
        res1 = form1.send_mail()

        form2 = self.form
        form2.is_valid()
        res2 = form2.send_mail()

        #Verifica se res1 e res2 possuem o mesmo retorno
        self.assertEquals(res1, res2)