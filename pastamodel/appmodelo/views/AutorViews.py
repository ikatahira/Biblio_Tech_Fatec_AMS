from django.shortcuts import render, redirect, get_object_or_404
from ..models import Autor
from ..forms import AutorForm

# Views para o modelo Autor
def lista_autores(request):
    autores = Autor.objects.all()
    return render(request, 'lista_autores.html', {'autores': autores})

def detalhes_autor(request, pk):
    autor = get_object_or_404(Autor, pk=pk)
    return render(request, 'detalhes_autor.html', {'autor': autor})

def novo_autor(request):
    if request.method == "POST":
        form = AutorForm(request.POST)
        if form.is_valid():
            autor = form.save()
            return redirect('detalhes_autor', pk=autor.pk)
    else:
        form = AutorForm()
    return render(request, 'editar_autor.html', {'form': form})

def editar_autor(request, pk):
    autor = get_object_or_404(Autor, pk=pk)
    if request.method == "POST":
        form = AutorForm(request.POST, instance=autor)
        if form.is_valid():
            autor = form.save()
            return redirect('detalhes_autor', pk=autor.pk)
    else:
        form = AutorForm(instance=autor)
    return render(request, 'editar_autor.html', {'form': form})

def deletar_autor(request, pk):
    autor = get_object_or_404(Autor, pk=pk)
    autor.delete()
    return redirect('lista_autores')