from django.shortcuts import render, redirect, get_object_or_404
from ..forms import Funcionario
from ..forms import FuncionarioForm

# Views para o modelo Funcionario
def lista_funcionarios(request):
    funcionarios = Funcionario.objects.all()
    return render(request, 'lista_funcionarios.html', {'funcionarios': funcionarios})

def detalhes_funcionario(request, pk):
    funcionario = get_object_or_404(Funcionario, pk=pk)
    return render(request, 'detalhes_funcionario.html', {'funcionario': funcionario})

def novo_funcionario(request):
    if request.method == "POST":
        form = FuncionarioForm(request.POST)
        if form.is_valid():
            funcionario = form.save()
            return redirect('detalhes_funcionario', pk=funcionario.pk)
    else:
        form = FuncionarioForm()
    return render(request, 'editar_funcionario.html', {'form': form})

def editar_funcionario(request, pk):
    funcionario = get_object_or_404(Funcionario, pk=pk)
    if request.method == "POST":
        form = FuncionarioForm(request.POST, instance=funcionario)
        if form.is_valid():
            funcionario = form.save()
            return redirect('detalhes_funcionario', pk=funcionario.pk)
    else:
        form = FuncionarioForm(instance=funcionario)
    return render(request, 'editar_funcionario.html', {'form': form})

def deletar_funcionario(request, pk):
    funcionario = get_object_or_404(Funcionario, pk=pk)
    funcionario.delete()
    return redirect('lista_funcionarios')