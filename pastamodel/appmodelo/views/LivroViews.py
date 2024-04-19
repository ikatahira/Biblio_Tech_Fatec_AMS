from django.shortcuts import render, redirect, get_object_or_404
from ..models import Livro
from ..forms import LivroForm

# Views para o modelo Livro
def lista_livros(request):
    livros = Livro.objects.all()
    return render(request, 'lista_livros.html', {'livros': livros})

def detalhes_livro(request, pk):
    livro = get_object_or_404(Livro, pk=pk)
    return render(request, 'detalhes_livro.html', {'livro': livro})

def novo_livro(request):
    if request.method == "POST":
        form = LivroForm(request.POST)
        if form.is_valid():
            livro = form.save()
            return redirect('detalhes_livro', pk=livro.pk)
    else:
        form = LivroForm()
    return render(request, 'editar_livro.html', {'form': form})

def editar_livro(request, pk):
    livro = get_object_or_404(Livro, pk=pk)
    if request.method == "POST":
        form = LivroForm(request.POST, instance=livro)
        if form.is_valid():
            livro = form.save()
            return redirect('detalhes_livro', pk=livro.pk)
    else:
        form = LivroForm(instance=livro)
    return render(request, 'editar_livro.html', {'form': form})

def deletar_livro(request, pk):
    livro = get_object_or_404(Livro, pk=pk)
    livro.delete()
    return redirect('lista_livros')