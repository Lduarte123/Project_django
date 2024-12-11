from django.shortcuts import render

# Create your views here.
def home (request):
    return render(request, 'home.html')

def contatos(request):
    return render(request, 'contatos.html')