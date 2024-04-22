# Views para o modelo Usuario
from django.shortcuts import render, redirect, get_object_or_404
from ..models import Usuario
from ..forms import UsuarioForm

def lista_usuarios(request):
    usuarios = Usuario.objects.all()
    return render(request, 'lista_usuarios.html', {'usuarios': usuarios})

def detalhes_usuario(request, pk):
    usuario = get_object_or_404(Usuario, pk=pk)
    return render(request, 'detalhes_usuario.html', {'usuario': usuario})

def novo_usuario(request):
    if request.method == "POST":
        form = UsuarioForm(request.POST)
        if form.is_valid():
            usuario = form.save()
            return redirect('detalhes_usuario', pk=usuario.pk)
    else:
        form = UsuarioForm()
    return render(request, 'editar_usuario.html', {'form': form})

def editar_usuario(request, pk):
    usuario = Usuario.objects.get(pk=pk)
    
    if request.method == "POST":
        form = UsuarioForm(request.POST, instance=usuario)
        if form.is_valid():
            form.save()
            return redirect('detalhes_usuario', pk=usuario.pk)
    else:
        form = UsuarioForm(instance=usuario)
    
    return render(request, 'editar_usuario.html', {'form': form})

def deletar_usuario(request, pk):
    usuario = get_object_or_404(Usuario, pk=pk)
    usuario.delete()
    return redirect('lista_usuarios')
