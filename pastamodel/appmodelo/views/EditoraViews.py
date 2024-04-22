from django.shortcuts import render, redirect, get_object_or_404
from ..models import Editora
from ..forms import EditoraForm

# Views para o modelo Editora
def lista_editoras(request):
    editoras = Editora.objects.all()
    return render(request, 'lista_editoras.html', {'editoras': editoras})

def detalhes_editora(request, pk):
    editora = get_object_or_404(Editora, pk=pk)
    return render(request, 'detalhes_editora.html', {'editora': editora})

def nova_editora(request):
    if request.method == "POST":
        form = EditoraForm(request.POST)
        if form.is_valid():
            editora = form.save()
            return redirect('detalhes_editora', pk=editora.pk)
    else:
        form = EditoraForm()
    return render(request, 'editar_editora.html', {'form': form})

def editar_editora(request, pk):
    editora = get_object_or_404(Editora, pk=pk)
    if request.method == "POST":
        form = EditoraForm(request.POST, instance=editora)
        if form.is_valid():
            editora = form.save()
            return redirect('detalhes_editora', pk=editora.pk)
    else:
        form = EditoraForm(instance=editora)
    return render(request, 'editar_editora.html', {'form': form})

def deletar_editora(request, pk):
    editora = get_object_or_404(Editora, pk=pk)
    editora.delete()
    return redirect('lista_editoras')