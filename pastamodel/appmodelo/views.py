# views.py

from django.shortcuts import render, redirect
from .forms import ClienteForm, ProdutoForm, PedidoForm
from .models import Cliente, Produto, Pedido
from django.http import HttpResponse
from django.shortcuts import render, redirect

def cadastrar_pedido(request):
    if request.method == 'POST':
        form = PedidoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_pedido')  # Supondo que haja uma view para listar os pedidos
    else:
        form = PedidoForm()
    return render(request, 'cadastrar_pedido.html', {'form': form})



def cadastrar_cliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_clientes')
    else:
        form = ClienteForm()
    return render(request, 'cadastrar_cliente.html', {'form': form})

def listar_clientes(request):
    clientes = Cliente.objects.all()
    return render(request, 'listar_clientes.html', {'clientes': clientes})


def cadastrar_produto(request):
    if request.method == 'POST':
        form = ProdutoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_produtos')
    else:
        form = ProdutoForm()
    return render(request, 'cadastrar_produto.html', {'form': form})

def listar_produtos(request):
    produtos = Produto.objects.all()
    return render(request, 'listar_produtos.html', {'produtos': produtos})

def pagina_inicial(request):
    pedidos = Pedido.objects.all()
    # Passa os pedidos como contexto para o template
    return render(request, 'pagina_inicial.html', {'pedidos': pedidos})


def listar_pedido(request):
    pedidos = Pedido.objects.all()
    return render(request, 'listar_pedido.html', {'pedidos': pedidos})

            
def deletar_pedido(request, pedido_id):
    # Lógica para deletar o pedido
    pedido = Pedido.objects.get(id=pedido_id)
    pedido.delete()
    # Redirecionar para a página de listar pedidos após a exclusão
    return redirect('listar_pedido')  # Alterado de 'listar_pedidos' para 'listar_pedido'

# Views para alterar e deletar cliente e produto
def alterar_cliente(request, cliente_id):
    cliente = Cliente.objects.get(id=cliente_id)
    if request.method == 'POST':
        form = ClienteForm(request.POST, instance=cliente)
        if form.is_valid():
            form.save()
        # Lógica para processar o formulário de alteração do cliente
            return redirect('listar_clientes')
    else:
        form = ClienteForm(instance=cliente)
    return render(request, 'alterar_cliente.html', {'form': form})

def alterar_produto(request, produto_id):
    produto = Produto.objects.get(id=produto_id)
    if request.method == 'POST':
        form = ProdutoForm(request.POST, instance=produto)
        if form.is_valid():
            form.save()
        # Lógica para processar o formulário de alteração do produto
        return redirect('listar_produtos')
    else:
        form = ProdutoForm(instance=produto)
    return render(request, 'alterar_produto.html', {'form': form})





def deletar_cliente(request, cliente_id):
    cliente = Cliente.objects.get(id=cliente_id)
    cliente.delete()
    return redirect('listar_clientes')


def deletar_produto(request, produto_id):
    produto = Produto.objects.get(id=produto_id)
    produto.delete()
    return redirect('listar_produtos')