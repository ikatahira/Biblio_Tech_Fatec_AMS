# Views para o modelo Genero
from django.shortcuts import render, redirect, get_object_or_404
from ..models import Genero
from ..forms import GeneroForm

def lista_generos(request):
    generos = Genero.objects.all()
    return render(request, 'lista_generos.html', {'generos': generos})

def detalhes_genero(request, pk):
    genero = get_object_or_404(Genero, pk=pk)
    return render(request, 'detalhes_genero.html', {'genero': genero})

def novo_genero(request):
    if request.method == "POST":
        form = GeneroForm(request.POST)
        if form.is_valid():
            genero = form.save()
            return redirect('detalhes_genero', pk=genero.pk)
    else:
        form = GeneroForm()
    return render(request, 'editar_genero.html', {'form': form})

def editar_genero(request, pk):
    genero = get_object_or_404(Genero, pk=pk)
    if request.method == "POST":
        form = GeneroForm(request.POST, instance=genero)
        if form.is_valid():
            genero = form.save()
            return redirect('detalhes_genero', pk=genero.pk)
    else:
        form = GeneroForm(instance=genero)
    return render(request, 'editar_genero.html', {'form': form})

def deletar_genero(request, pk):
    genero = get_object_or_404(Genero, pk=pk)
    genero.delete()
    return redirect('lista_generos')