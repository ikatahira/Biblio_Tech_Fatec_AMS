from django.shortcuts import render, redirect, get_object_or_404
from ..forms import Comentario
from ..forms import ComentarioForm
from django.utils import timezone

# Views para o modelo Comentario
def lista_comentarios(request):
    comentarios = Comentario.objects.all()
    return render(request, 'lista_comentarios.html', {'comentarios': comentarios})

def detalhes_comentario(request, pk):
    comentario = get_object_or_404(Comentario, pk=pk)
    return render(request, 'detalhes_comentario.html', {'comentario': comentario})

def novo_comentario(request):
    if request.method == "POST":
        form = ComentarioForm(request.POST)
        if form.is_valid():
            # Obtém a data e hora atual em horário de Brasília
            data_hora_atual_brasilia = timezone.localtime(timezone.now(), timezone=timezone.get_current_timezone())
            # Define a data do comentário como a data e hora atual
            form.instance.data_comentario = data_hora_atual_brasilia
            # Salva o comentário
            comentario = form.save()
            return redirect('detalhes_comentario', pk=comentario.pk)
    else:
        form = ComentarioForm()
    return render(request, 'editar_comentario.html', {'form': form})

def editar_comentario(request, pk):
    comentario = get_object_or_404(Comentario, pk=pk)
    if request.method == "POST":
        form = ComentarioForm(request.POST, instance=comentario)
        if form.is_valid():
            comentario = form.save()
            return redirect('detalhes_comentario', pk=comentario.pk)
    else:
        form = ComentarioForm(instance=comentario)
    return render(request, 'editar_comentario.html', {'form': form})

def deletar_comentario(request, pk):
    comentario = get_object_or_404(Comentario, pk=pk)
    comentario.delete()
    return redirect('lista_comentarios')