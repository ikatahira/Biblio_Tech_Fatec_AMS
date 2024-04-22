from django.shortcuts import render, redirect, get_object_or_404
from ..forms import Exemplar
from ..forms import ExemplarForm

# Views para o modelo Exemplar
def lista_exemplares(request):
    exemplares = Exemplar.objects.all()
    return render(request, 'lista_exemplares.html', {'exemplares': exemplares})

def detalhes_exemplar(request, pk):
    exemplar = get_object_or_404(Exemplar, pk=pk)
    return render(request, 'detalhes_exemplar.html', {'exemplar': exemplar})

def novo_exemplar(request):
    if request.method == "POST":
        form = ExemplarForm(request.POST)
        if form.is_valid():
            exemplar = form.save()
            return redirect('detalhes_exemplar', pk=exemplar.pk)
    else:
        form = ExemplarForm()
    return render(request, 'editar_exemplar.html', {'form': form})

def editar_exemplar(request, pk):
    exemplar = get_object_or_404(Exemplar, pk=pk)
    if request.method == "POST":
        form = ExemplarForm(request.POST, instance=exemplar)
        if form.is_valid():
            exemplar = form.save()
            return redirect('detalhes_exemplar', pk=exemplar.pk)
    else:
        form = ExemplarForm(instance=exemplar)
    return render(request, 'editar_exemplar.html', {'form': form})

def deletar_exemplar(request, pk):
    exemplar = get_object_or_404(Exemplar, pk=pk)
    exemplar.delete()
    return redirect('lista_exemplares')