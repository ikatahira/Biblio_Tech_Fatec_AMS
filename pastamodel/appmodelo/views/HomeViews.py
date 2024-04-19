from django.shortcuts import render
from ..models import Livro

def home(request):
    # Use o nome correto do campo de data de publicação
    livros_recentes = Livro.objects.all().order_by('-ano_publicacao')

    # Renderizar a página inicial com os livros recentes
    return render(request, 'base.html', {'livros_recentes': livros_recentes})



