from django.shortcuts import render, redirect, get_object_or_404
from ..forms import Multa
from ..forms import MultaForm

# Views para o modelo Multa
def lista_multas(request):
    multas = Multa.objects.all()
    return render(request, 'lista_multas.html', {'multas': multas})

def detalhes_multa(request, pk):
    multa = get_object_or_404(Multa, pk=pk)
    return render(request, 'detalhes_multa.html', {'multa': multa})

def nova_multa(request):
    if request.method == "POST":
        form = MultaForm(request.POST)
        if form.is_valid():
            multa = form.save()
            return redirect('detalhes_multa', pk=multa.pk)
    else:
        form = MultaForm()
    return render(request, 'editar_multa.html', {'form': form})

def editar_multa(request, pk):
    multa = get_object_or_404(Multa, pk=pk)
    if request.method == "POST":
        form = MultaForm(request.POST, instance=multa)
        if form.is_valid():
            multa = form.save()
            return redirect('detalhes_multa', pk=multa.pk)
    else:
        form = MultaForm(instance=multa)
    return render(request, 'editar_multa.html', {'form': form})

def deletar_multa(request, pk):
    multa = get_object_or_404(Multa, pk=pk)
    multa.delete()
    return redirect('lista_multas')