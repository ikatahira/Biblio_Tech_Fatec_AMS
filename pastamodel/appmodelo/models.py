from django.db import models

class Genero(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class Editora(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class Autor(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class Livro(models.Model):
    titulo = models.CharField(max_length=200)
    ano_publicacao = models.IntegerField()
    genero = models.ForeignKey(Genero, on_delete=models.CASCADE)
    editora = models.ForeignKey(Editora, on_delete=models.CASCADE)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo

class Exemplar(models.Model):
    livro = models.ForeignKey(Livro, on_delete=models.CASCADE)
    num_serie = models.CharField(max_length=100)
    data_aquisicao = models.DateField()

    def __str__(self):
        return f"{self.livro.titulo} - {self.num_serie}"

class Funcionario(models.Model):
    nome = models.CharField(max_length=100)
    sobrenome = models.CharField(max_length=100)
    cargo = models.CharField(max_length=100)
    data_contratacao = models.DateField()

    def __str__(self):
        return f"{self.nome} {self.sobrenome}"

class Usuario(models.Model):
    nome = models.CharField(max_length=100)
    sobrenome = models.CharField(max_length=100)
    data_nascimento = models.DateField()
    endereco = models.TextField()
    email = models.EmailField()
    telefone = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.nome} {self.sobrenome}"

class Emprestimo(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    exemplar = models.ForeignKey(Exemplar, on_delete=models.CASCADE)
    data_emprestimo = models.DateField()
    data_devolucao_prevista = models.DateField()
    data_devolucao_real = models.DateField(blank=True, null=True)
    status = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.exemplar} - {self.usuario}"

class Multa(models.Model):
    emprestimo = models.ForeignKey(Emprestimo, on_delete=models.CASCADE)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    data_pagamento = models.DateField(blank=True, null=True)
    status = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.emprestimo} - {self.valor}"

class Comentario(models.Model):
    livro = models.ForeignKey(Livro, on_delete=models.CASCADE)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    comentario = models.TextField()
    classificacao = models.CharField(max_length=100)
    data_comentario = models.DateField()

    def __str__(self):
        return f"{self.livro} - {self.usuario}"

class Avaliacao(models.Model):
    livro = models.ForeignKey(Livro, on_delete=models.CASCADE)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    avaliacao = models.IntegerField()
    data_avaliacao = models.DateField()

    def __str__(self):
        return f"{self.livro} - {self.usuario}"

class FuncLivro(models.Model):
    funcionario = models.ForeignKey(Funcionario, on_delete=models.CASCADE)
    livro = models.ForeignKey(Livro, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.funcionario} - {self.livro}"

class Reserva(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    livro = models.ForeignKey(Livro, on_delete=models.CASCADE)
    data_reserva = models.DateField()
    status = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.usuario} - {self.livro}"

class Log(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    data_hora = models.DateTimeField(auto_now_add=True)
    acao_realizada = models.CharField(max_length=100)
    descricao = models.TextField()

    def __str__(self):
        return f"{self.usuario} - {self.data_hora}"
