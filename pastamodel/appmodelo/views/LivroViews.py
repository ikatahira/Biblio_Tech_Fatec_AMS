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
        form = LivroForm(request.POST, request.FILES)
        if form.is_valid():
            livro = form.save(commit=False)  # Salvar o formulário, mas não o objeto ainda
            if 'imagem' in request.FILES:  # Verificar se o arquivo de imagem foi enviado
                livro.imagem = request.FILES['imagem']  # Atribuir o arquivo de imagem ao campo do modelo
            livro.save()  # Agora, salvar o objeto do livro com o arquivo de imagem
            return redirect('detalhes_livro', pk=livro.pk)
    else:
        form = LivroForm()
    return render(request, 'editar_livro.html', {'form': form})


def editar_livro(request, pk):
    livro = get_object_or_404(Livro, pk=pk)
    if request.method == "POST":
        form = LivroForm(request.POST, request.FILES, instance=livro)  # Passando request.FILES para processar os arquivos enviados
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

def livros_recentes(request):
    livros = Livro.objects.all().order_by('-data_publicacao')  

    return render(request, 'livros_recentes.html', {'livros': livros})