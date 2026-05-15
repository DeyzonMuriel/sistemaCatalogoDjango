from django.shortcuts import render

# Create your views here.
def listaFilmes(request):
    return render(request, 'filmes/lista.html')

def detalheFilme(request):
    return render(request, 'filmes/detalhe.html')