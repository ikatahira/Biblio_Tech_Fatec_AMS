from django.shortcuts import render, redirect, get_object_or_404
from ..forms import FuncLivro
from ..forms import FuncLivroForm

# Views para o modelo FuncLivro
def lista_func_livros(request):
    func_livros = FuncLivro.objects.all()
    return render(request, 'lista_func_livros.html', {'func_livros': func_livros})

def detalhes_func_livro(request, pk):
    func_livro = get_object_or_404(FuncLivro, pk=pk)
    return render(request, 'detalhes_func_livro.html', {'func_livro': func_livro})

def novo_func_livro(request):
    if request.method == "POST":
        form = FuncLivroForm(request.POST)
        if form.is_valid():
            func_livro = form.save()
            return redirect('detalhes_func_livro', pk=func_livro.pk)
    else:
        form = FuncLivroForm()
    return render(request, 'editar_func_livro.html', {'form': form})

def editar_func_livro(request, pk):
    func_livro = get_object_or_404(FuncLivro, pk=pk)
    if request.method == "POST":
        form = FuncLivroForm(request.POST, instance=func_livro)
        if form.is_valid():
            func_livro = form.save()
            return redirect('detalhes_func_livro', pk=func_livro.pk)
    else:
        form = FuncLivroForm(instance=func_livro)
    return render(request, 'editar_func_livro.html', {'form': form})

def deletar_func_livro(request, pk):
    func_livro = get_object_or_404(FuncLivro, pk=pk)
    func_livro.delete()
    return redirect('lista_func_livros')