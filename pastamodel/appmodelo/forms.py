from django import forms
from .models import Genero, Editora, Autor, Livro, Exemplar, Funcionario, Usuario, Emprestimo, Multa, Comentario, Avaliacao, FuncLivro, Reserva, Log

class GeneroForm(forms.ModelForm):
    class Meta:
        model = Genero
        fields = ['nome']

class EditoraForm(forms.ModelForm):
    class Meta:
        model = Editora
        fields = ['nome']

class AutorForm(forms.ModelForm):
    class Meta:
        model = Autor
        fields = ['nome']

class LivroForm(forms.ModelForm):
    class Meta:
        model = Livro
        fields = ['titulo', 'ano_publicacao', 'genero', 'editora', 'autor']

class ExemplarForm(forms.ModelForm):
    class Meta:
        model = Exemplar
        fields = ['livro', 'num_serie', 'data_aquisicao']

class FuncionarioForm(forms.ModelForm):
    class Meta:
        model = Funcionario
        fields = ['nome', 'sobrenome', 'cargo', 'data_contratacao']

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['nome', 'sobrenome', 'data_nascimento', 'endereco', 'email', 'telefone']

class EmprestimoForm(forms.ModelForm):
    class Meta:
        model = Emprestimo
        fields = ['usuario', 'exemplar', 'data_emprestimo', 'data_devolucao_prevista', 'data_devolucao_real', 'status']

class MultaForm(forms.ModelForm):
    class Meta:
        model = Multa
        fields = ['emprestimo', 'valor', 'data_pagamento', 'status']

class ComentarioForm(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ['livro', 'usuario', 'comentario', 'classificacao', 'data_comentario']

class AvaliacaoForm(forms.ModelForm):
    class Meta:
        model = Avaliacao
        fields = ['livro', 'usuario', 'avaliacao', 'data_avaliacao']

class FuncLivroForm(forms.ModelForm):
    class Meta:
        model = FuncLivro
        fields = ['funcionario', 'livro']

class ReservaForm(forms.ModelForm):
    class Meta:
        model = Reserva
        fields = ['usuario', 'livro', 'data_reserva', 'status']

class LogForm(forms.Form):
    acao_realizada = forms.CharField(label='Ação Realizada', max_length=100)
    descricao = forms.CharField(label='Descrição', widget=forms.Textarea)
