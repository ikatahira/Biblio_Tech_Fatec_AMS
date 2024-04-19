from django.shortcuts import render, redirect, get_object_or_404
from ..forms import Emprestimo
from ..forms import EmprestimoForm

# Views para o modelo Emprestimo
def lista_emprestimos(request):
    emprestimos = Emprestimo.objects.all()
    return render(request, 'lista_emprestimos.html', {'emprestimos': emprestimos})

def detalhes_emprestimo(request, pk):
    emprestimo = get_object_or_404(Emprestimo, pk=pk)
    return render(request, 'detalhes_emprestimo.html', {'emprestimo': emprestimo})

def novo_emprestimo(request):
    if request.method == "POST":
        form = EmprestimoForm(request.POST)
        if form.is_valid():
            emprestimo = form.save()
            return redirect('detalhes_emprestimo', pk=emprestimo.pk)
    else:
        form = EmprestimoForm()
    return render(request, 'editar_emprestimo.html', {'form': form})

def editar_emprestimo(request, pk):
    emprestimo = get_object_or_404(Emprestimo, pk=pk)
    if request.method == "POST":
        form = EmprestimoForm(request.POST, instance=emprestimo)
        if form.is_valid():
            emprestimo = form.save()
            return redirect('detalhes_emprestimo', pk=emprestimo.pk)
    else:
        form = EmprestimoForm(instance=emprestimo)
    return render(request, 'editar_emprestimo.html', {'form': form})

def deletar_emprestimo(request, pk):
    emprestimo = get_object_or_404(Emprestimo, pk=pk)
    emprestimo.delete()
    return redirect('lista_emprestimos')