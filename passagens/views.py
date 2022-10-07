from django.shortcuts import render

from passagens.forms import PassagemForm

def index(request):
    form = PassagemForm()
    contexto = {'form': form,}
    return render(request, 'index.html', contexto)
