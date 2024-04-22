from django.shortcuts import render, redirect, get_object_or_404
from ..forms import Avaliacao
from ..forms import AvaliacaoForm

# Views para o modelo Avaliacao
def lista_avaliacoes(request):
    avaliacoes = Avaliacao.objects.all()
    return render(request, 'lista_avaliacoes.html', {'avaliacoes': avaliacoes})

def detalhes_avaliacao(request, pk):
    avaliacao = get_object_or_404(Avaliacao, pk=pk)
    return render(request, 'detalhes_avaliacao.html', {'avaliacao': avaliacao})

def nova_avaliacao(request):
    if request.method == "POST":
        form = AvaliacaoForm(request.POST)
        if form.is_valid():
            avaliacao = form.save()
            return redirect('detalhes_avaliacao', pk=avaliacao.pk)
    else:
        form = AvaliacaoForm()
    return render(request, 'editar_avaliacao.html', {'form': form})

def editar_avaliacao(request, pk):
    avaliacao = get_object_or_404(Avaliacao, pk=pk)
    if request.method == "POST":
        form = AvaliacaoForm(request.POST, instance=avaliacao)
        if form.is_valid():
            avaliacao = form.save()
            return redirect('detalhes_avaliacao', pk=avaliacao.pk)
    else:
        form = AvaliacaoForm(instance=avaliacao)
    return render(request, 'editar_avaliacao.html', {'form': form})

def deletar_avaliacao(request, pk):
    avaliacao = get_object_or_404(Avaliacao, pk=pk)
    avaliacao.delete()
    return redirect('lista_avaliacoes')