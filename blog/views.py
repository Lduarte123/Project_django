from django.shortcuts import render

# Create your views here.
def home (request):
    return render(request, 'home.html')

def contatos(request):
    return render(request, 'contatos.html')

def habilidades(request):
    return render(request, 'habilidades.html')

def sobre(request):
    return render(request, 'sobre.html')

def projetos(request):
    return render(request, 'projetos.html')