from django import forms
from tempus_dominus.widgets import DatePicker
from datetime import datetime
from passagens.classe_viagem import tipos_de_classes
from .validation import * # Importa todas as funções e classes do pacote validation.

from .models import Passagem, ClasseViagem, Pessoa

class PassagemForm(forms.ModelForm):
    data_pesquisa = forms.DateField(label='Data da pesquisa', disabled=True, initial=datetime.today)
    class Meta:
        model = Passagem
        fields = '__all__'
        labels = {
            'data_ida' : "Data de ida",
            'data_volta' : "Data de volta",
            'data_pesquisa' : "Data da pesequisa",
            'informacoes' : "Informações",
            'classe_viagem' : "Classe do voo",
        }
        widgets = {
            'informacoes': forms.Textarea(),
            'data_ida' : DatePicker(),
            'data_volta' : DatePicker(),
        }

    # O método clean faz a validação em conjunto;
    # Já os métodos clean_[campo] validam cada campo individualmente.
    def clean(self):
        origem = self.cleaned_data.get('origem')
        destino = self.cleaned_data.get('destino')
        data_ida = self.cleaned_data.get('data_ida')
        data_volta = self.cleaned_data.get('data_volta')
        data_pesquisa = self.cleaned_data.get('data_pesquisa')
        lista_de_erros = {}
        campo_tem_algum_numero(origem, 'origem', lista_de_erros)
        campo_tem_algum_numero(destino, 'destino', lista_de_erros)
        origem_destino_iguais(origem, destino, lista_de_erros)
        data_ida_maior_que_data_volta(data_ida, data_volta, lista_de_erros)
        data_ida_menor_data_de_hoje(data_ida, data_pesquisa, lista_de_erros)
        for nome_campo in lista_de_erros:
            mensagem_erro = lista_de_erros[nome_campo]
            self.add_error(nome_campo, mensagem_erro)
        return self.cleaned_data

class PessoaForm(forms.ModelForm):
    class Meta:
        model = Pessoa
        exclude = ['nome']
