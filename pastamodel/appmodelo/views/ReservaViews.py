from django.shortcuts import render, redirect, get_object_or_404
from ..forms import Reserva
from ..forms import ReservaForm

# Views para o modelo Reserva
def lista_reservas(request):
    reservas = Reserva.objects.all()
    return render(request, 'lista_reservas.html', {'reservas': reservas})

def detalhes_reserva(request, pk):
    reserva = get_object_or_404(Reserva, pk=pk)
    return render(request, 'detalhes_reserva.html', {'reserva': reserva})

def nova_reserva(request):
    if request.method == "POST":
        form = ReservaForm(request.POST)
        if form.is_valid():
            reserva = form.save()
            return redirect('detalhes_reserva', pk=reserva.pk)
    else:
        form = ReservaForm()
    return render(request, 'editar_reserva.html', {'form': form})

def editar_reserva(request, pk):
    reserva = get_object_or_404(Reserva, pk=pk)
    if request.method == "POST":
        form = ReservaForm(request.POST, instance=reserva)
        if form.is_valid():
            reserva = form.save()
            return redirect('detalhes_reserva', pk=reserva.pk)
    else:
        form = ReservaForm(instance=reserva)
    return render(request, 'editar_reserva.html', {'form': form})

def deletar_reserva(request, pk):
    reserva = get_object_or_404(Reserva, pk=pk)
    reserva.delete()
    return redirect('lista_reservas')