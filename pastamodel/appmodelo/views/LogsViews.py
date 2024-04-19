from django.shortcuts import render, redirect, get_object_or_404
from ..forms import Log
from ..forms import LogForm

# Views para o modelo Log
def lista_logs(request):
    logs = Log.objects.all()
    return render(request, 'lista_logs.html', {'logs': logs})

def detalhes_log(request, pk):
    log = get_object_or_404(Log, pk=pk)
    return render(request, 'detalhes_log.html', {'log': log})

def novo_log(request):
    if request.method == "POST":
        form = LogForm(request.POST)
        if form.is_valid():
            log = form.save()
            return redirect('detalhes_log', pk=log.pk)
    else:
        form = LogForm()
    return render(request, 'editar_log.html', {'form': form})

def editar_log(request, pk):
    log = get_object_or_404(Log, pk=pk)
    if request.method == "POST":
        form = LogForm(request.POST, instance=log)
        if form.is_valid():
            log = form.save()
            return redirect('detalhes_log', pk=log.pk)
    else:
        form = LogForm(instance=log)
    return render(request, 'editar_log.html', {'form': form})

def deletar_log(request, pk):
    log = get_object_or_404(Log, pk=pk)
    log.delete()
    return redirect('lista_logs')