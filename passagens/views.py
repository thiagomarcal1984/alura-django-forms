from django.shortcuts import render

from passagens.forms import PassagemForm, PessoaForm

def index(request):
    form = PassagemForm()
    pessoa_form = PessoaForm()
    contexto = {
        'form': form,
        'pessoa_form': pessoa_form,
    }
    return render(request, 'index.html', contexto)

def revisao_consulta(request):
    if request.method == 'POST':
        form=PassagemForm(request.POST)
        pessoa_form=PessoaForm(request.POST)
        contexto = {
            'form': form,
            'pessoa_form': pessoa_form,
        }
        if form.is_valid() and pessoa_form.is_valid:
            return render(request, 'minha_consulta.html', contexto)
        else:
            print('Form inválido.')            
            return render(request, 'index.html', contexto)
