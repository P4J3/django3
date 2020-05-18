from django import forms

from django.core.mail.message import EmailMessage



class ContatoForm(forms.Form):

    #Cria as varíaveis e o próprio Form cria um dicionário onde as chaves possuem o
    #mesmo nome que as variáveis

    nome = forms.CharField(label='Nome', max_length=100)
    email = forms.EmailField(label='E-mail', max_length=100)
    assunto = forms.CharField(label='Assunto', max_length=100)
    mensagem = forms.CharField(label='Mensagem', widget=forms.Textarea())

    def send_mail(self):
        #Pega o dicionário criado a cima e passa os valores que estão nas chaves para as variáveis
        nome = self.cleaned_data['nome']
        email = self.cleaned_data['email']
        assunto = self.cleaned_data['assunto']
        mensagem = self.cleaned_data['mensagem']

        #Montando a mensagem
        conteudo = f'Nome: {nome}\nEmail: {email}\nAssunto: {assunto}\nMensagem: {mensagem}'

        #preparando o email para ser enviado
        mail = EmailMessage(
            subject=assunto,
            body=conteudo,
            from_email='algo@outlook.com',
            to=['alguem@outlook.com',],
            headers={'Reply-To': email}
        )
        mail.send()

