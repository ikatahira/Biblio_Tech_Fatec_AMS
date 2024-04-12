from django.shortcuts import render, redirect, get_object_or_404
from .models import Genero, Editora, Autor, Livro, Exemplar, Funcionario, Usuario, Emprestimo, Multa, Comentario, Avaliacao, FuncLivro, Reserva, Log
from .forms import GeneroForm, EditoraForm, AutorForm, LivroForm, ExemplarForm, FuncionarioForm, UsuarioForm, EmprestimoForm, MultaForm, ComentarioForm, AvaliacaoForm, FuncLivroForm, ReservaForm, LogForm

def home(request):
    return render(request, 'home.html')
# Views para o modelo Genero
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


# Views para o modelo Editora
def lista_editoras(request):
    editoras = Editora.objects.all()
    return render(request, 'lista_editoras.html', {'editoras': editoras})

def detalhes_editora(request, pk):
    editora = get_object_or_404(Editora, pk=pk)
    return render(request, 'detalhes_editora.html', {'editora': editora})

def nova_editora(request):
    if request.method == "POST":
        form = EditoraForm(request.POST)
        if form.is_valid():
            editora = form.save()
            return redirect('detalhes_editora', pk=editora.pk)
    else:
        form = EditoraForm()
    return render(request, 'editar_editora.html', {'form': form})

def editar_editora(request, pk):
    editora = get_object_or_404(Editora, pk=pk)
    if request.method == "POST":
        form = EditoraForm(request.POST, instance=editora)
        if form.is_valid():
            editora = form.save()
            return redirect('detalhes_editora', pk=editora.pk)
    else:
        form = EditoraForm(instance=editora)
    return render(request, 'editar_editora.html', {'form': form})

def deletar_editora(request, pk):
    editora = get_object_or_404(Editora, pk=pk)
    editora.delete()
    return redirect('lista_editoras')


# Views para o modelo Autor
def lista_autores(request):
    autores = Autor.objects.all()
    return render(request, 'lista_autores.html', {'autores': autores})

def detalhes_autor(request, pk):
    autor = get_object_or_404(Autor, pk=pk)
    return render(request, 'detalhes_autor.html', {'autor': autor})

def novo_autor(request):
    if request.method == "POST":
        form = AutorForm(request.POST)
        if form.is_valid():
            autor = form.save()
            return redirect('detalhes_autor', pk=autor.pk)
    else:
        form = AutorForm()
    return render(request, 'editar_autor.html', {'form': form})

def editar_autor(request, pk):
    autor = get_object_or_404(Autor, pk=pk)
    if request.method == "POST":
        form = AutorForm(request.POST, instance=autor)
        if form.is_valid():
            autor = form.save()
            return redirect('detalhes_autor', pk=autor.pk)
    else:
        form = AutorForm(instance=autor)
    return render(request, 'editar_autor.html', {'form': form})

def deletar_autor(request, pk):
    autor = get_object_or_404(Autor, pk=pk)
    autor.delete()
    return redirect('lista_autores')


# Views para o modelo Livro
def lista_livros(request):
    livros = Livro.objects.all()
    return render(request, 'lista_livros.html', {'livros': livros})

def detalhes_livro(request, pk):
    livro = get_object_or_404(Livro, pk=pk)
    return render(request, 'detalhes_livro.html', {'livro': livro})

def novo_livro(request):
    if request.method == "POST":
        form = LivroForm(request.POST)
        if form.is_valid():
            livro = form.save()
            return redirect('detalhes_livro', pk=livro.pk)
    else:
        form = LivroForm()
    return render(request, 'editar_livro.html', {'form': form})

def editar_livro(request, pk):
    livro = get_object_or_404(Livro, pk=pk)
    if request.method == "POST":
        form = LivroForm(request.POST, instance=livro)
        if form.is_valid():
            livro = form.save()
            return redirect('detalhes_livro', pk=livro.pk)
    else:
        form = LivroForm(instance=livro)
    return render(request, 'editar_livro.html', {'form': form})

def deletar_livro(request, pk):
    livro = get_object_or_404(Livro, pk=pk)
    livro.delete()
    return redirect('lista_livros')


# Views para o modelo Exemplar
def lista_exemplares(request):
    exemplares = Exemplar.objects.all()
    return render(request, 'lista_exemplares.html', {'exemplares': exemplares})

def detalhes_exemplar(request, pk):
    exemplar = get_object_or_404(Exemplar, pk=pk)
    return render(request, 'detalhes_exemplar.html', {'exemplar': exemplar})

def novo_exemplar(request):
    if request.method == "POST":
        form = ExemplarForm(request.POST)
        if form.is_valid():
            exemplar = form.save()
            return redirect('detalhes_exemplar', pk=exemplar.pk)
    else:
        form = ExemplarForm()
    return render(request, 'editar_exemplar.html', {'form': form})

def editar_exemplar(request, pk):
    exemplar = get_object_or_404(Exemplar, pk=pk)
    if request.method == "POST":
        form = ExemplarForm(request.POST, instance=exemplar)
        if form.is_valid():
            exemplar = form.save()
            return redirect('detalhes_exemplar', pk=exemplar.pk)
    else:
        form = ExemplarForm(instance=exemplar)
    return render(request, 'editar_exemplar.html', {'form': form})

def deletar_exemplar(request, pk):
    exemplar = get_object_or_404(Exemplar, pk=pk)
    exemplar.delete()
    return redirect('lista_exemplares')


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


# Views para o modelo Usuario
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
    usuario = get_object_or_404(Usuario, pk=pk)
    if request.method == "POST":
        form = UsuarioForm(request.POST, instance=usuario)
        if form.is_valid():
            usuario = form.save()
            return redirect('detalhes_usuario', pk=usuario.pk)
    else:
        form = UsuarioForm(instance=usuario)
    return render(request, 'editar_usuario.html', {'form': form})

def deletar_usuario(request, pk):
    usuario = get_object_or_404(Usuario, pk=pk)
    usuario.delete()
    return redirect('lista_usuarios')


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


# Views para o modelo FuncLivro
def lista_func_livros(request):
    func_livros = FuncLivro.objects.all()
    return render(request, 'lista_func_livros.html', {'func_livros': func_livros})

def detalhes_func_livro(request, pk):
    func_livro = get_object_or_404(FuncLivro, pk=pk)
    return render(request, 'detalhes_func_livro.html', {'func_livro': func_livro})

def novo_func_livro(request):
    if request.method == "POST":
        form = FuncLivroForm(request.POST)
        if form.is_valid():
            func_livro = form.save()
            return redirect('detalhes_func_livro', pk=func_livro.pk)
    else:
        form = FuncLivroForm()
    return render(request, 'editar_func_livro.html', {'form': form})

def editar_func_livro(request, pk):
    func_livro = get_object_or_404(FuncLivro, pk=pk)
    if request.method == "POST":
        form = FuncLivroForm(request.POST, instance=func_livro)
        if form.is_valid():
            func_livro = form.save()
            return redirect('detalhes_func_livro', pk=func_livro.pk)
    else:
        form = FuncLivroForm(instance=func_livro)
    return render(request, 'editar_func_livro.html', {'form': form})

def deletar_func_livro(request, pk):
    func_livro = get_object_or_404(FuncLivro, pk=pk)
    func_livro.delete()
    return redirect('lista_func_livros')


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

# As views para os outros modelos continuam aqui...

