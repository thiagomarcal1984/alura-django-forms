from django.shortcuts import render

from passagens.forms import PassagemForm

def index(request):
    form = PassagemForm()
    contexto = {'form': form,}
    return render(request, 'index.html', contexto)

def revisao_consulta(request):
    if request.method == 'POST':
        form=PassagemForm(request.POST)
        contexto = {'form': form,}
        if form.is_valid():
            return render(request, 'minha_consulta.html', contexto)
        else:
            print('Form inválido.')            
            return render(request, 'index.html', contexto)
