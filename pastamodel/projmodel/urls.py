from django.urls import path
from appmodelo import views

   
urlpatterns = [
    path('', views.home, name='home'),
    # URLs para o modelo Genero
    path('generos/', views.lista_generos, name='lista_generos'),
    path('genero/<int:pk>/', views.detalhes_genero, name='detalhes_genero'),
    path('genero/novo/', views.novo_genero, name='novo_genero'),
    path('genero/editar/<int:pk>/', views.editar_genero, name='editar_genero'),
    path('genero/deletar/<int:pk>/', views.deletar_genero, name='deletar_genero'),

    # URLs para o modelo Editora
    path('editoras/', views.lista_editoras, name='lista_editoras'),
    path('editora/<int:pk>/', views.detalhes_editora, name='detalhes_editora'),
    path('editora/nova/', views.nova_editora, name='nova_editora'),
    path('editora/editar/<int:pk>/', views.editar_editora, name='editar_editora'),
    path('editora/deletar/<int:pk>/', views.deletar_editora, name='deletar_editora'),

    # URLs para o modelo Autor
    path('autores/', views.lista_autores, name='lista_autores'),
    path('autor/<int:pk>/', views.detalhes_autor, name='detalhes_autor'),
    path('autor/novo/', views.novo_autor, name='novo_autor'),
    path('autor/editar/<int:pk>/', views.editar_autor, name='editar_autor'),
    path('autor/deletar/<int:pk>/', views.deletar_autor, name='deletar_autor'),

    # URLs para o modelo Livro
    path('livros/', views.lista_livros, name='lista_livros'),
    path('livro/<int:pk>/', views.detalhes_livro, name='detalhes_livro'),
    path('livro/novo/', views.novo_livro, name='novo_livro'),
    path('livro/editar/<int:pk>/', views.editar_livro, name='editar_livro'),
    path('livro/deletar/<int:pk>/', views.deletar_livro, name='deletar_livro'),

    # URLs para o modelo Exemplar
    path('exemplares/', views.lista_exemplares, name='lista_exemplares'),
    path('exemplar/<int:pk>/', views.detalhes_exemplar, name='detalhes_exemplar'),
    path('exemplar/novo/', views.novo_exemplar, name='novo_exemplar'),
    path('exemplar/editar/<int:pk>/', views.editar_exemplar, name='editar_exemplar'),
    path('exemplar/deletar/<int:pk>/', views.deletar_exemplar, name='deletar_exemplar'),

    # URLs para o modelo Funcionario
    path('funcionarios/', views.lista_funcionarios, name='lista_funcionarios'),
    path('funcionario/<int:pk>/', views.detalhes_funcionario, name='detalhes_funcionario'),
    path('funcionario/novo/', views.novo_funcionario, name='novo_funcionario'),
    path('funcionario/editar/<int:pk>/', views.editar_funcionario, name='editar_funcionario'),
    path('funcionario/deletar/<int:pk>/', views.deletar_funcionario, name='deletar_funcionario'),

    # URLs para o modelo Usuario
    path('usuarios/', views.lista_usuarios, name='lista_usuarios'),
    path('usuario/<int:pk>/', views.detalhes_usuario, name='detalhes_usuario'),
    path('usuario/novo/', views.novo_usuario, name='novo_usuario'),
    path('usuario/editar/<int:pk>/', views.editar_usuario, name='editar_usuario'),
    path('usuario/deletar/<int:pk>/', views.deletar_usuario, name='deletar_usuario'),

    # URLs para o modelo Emprestimo
    path('emprestimos/', views.lista_emprestimos, name='lista_emprestimos'),
    path('emprestimo/<int:pk>/', views.detalhes_emprestimo, name='detalhes_emprestimo'),
    path('emprestimo/novo/', views.novo_emprestimo, name='novo_emprestimo'),
    path('emprestimo/editar/<int:pk>/', views.editar_emprestimo, name='editar_emprestimo'),
    path('emprestimo/deletar/<int:pk>/', views.deletar_emprestimo, name='deletar_emprestimo'),

    # URLs para o modelo Multa
    path('multas/', views.lista_multas, name='lista_multas'),
    path('multa/<int:pk>/', views.detalhes_multa, name='detalhes_multa'),
    path('multa/nova/', views.nova_multa, name='nova_multa'),
    path('multa/editar/<int:pk>/', views.editar_multa, name='editar_multa'),
    path('multa/deletar/<int:pk>/', views.deletar_multa, name='deletar_multa'),

    # URLs para o modelo Comentario
    path('comentarios/', views.lista_comentarios, name='lista_comentarios'),
    path('comentario/<int:pk>/', views.detalhes_comentario, name='detalhes_comentario'),
    path('comentario/novo/', views.novo_comentario, name='novo_comentario'),
    path('comentario/editar/<int:pk>/', views.editar_comentario, name='editar_comentario'),
    path('comentario/deletar/<int:pk>/', views.deletar_comentario, name='deletar_comentario'),

    # URLs para o modelo Avaliacao
    path('avaliacoes/', views.lista_avaliacoes, name='lista_avaliacoes'),
    path('avaliacao/<int:pk>/', views.detalhes_avaliacao, name='detalhes_avaliacao'),
    path('avaliacao/nova/', views.nova_avaliacao, name='nova_avaliacao'),
    path('avaliacao/editar/<int:pk>/', views.editar_avaliacao, name='editar_avaliacao'),
    path('avaliacao/deletar/<int:pk>/', views.deletar_avaliacao, name='deletar_avaliacao'),

    # URLs para o modelo FuncLivro
    path('funclivros/', views.lista_func_livros, name='lista_func_livros'),
    path('funclivro/<int:pk>/', views.detalhes_func_livro, name='detalhes_func_livro'),
    path('funclivro/novo/', views.novo_func_livro, name='novo_func_livro'),
    path('funclivro/editar/<int:pk>/', views.editar_func_livro, name='editar_func_livro'),
    path('funclivro/deletar/<int:pk>/', views.deletar_func_livro, name='deletar_func_livro'),

    # URLs para o modelo Reserva
    path('reservas/', views.lista_reservas, name='lista_reservas'),
    path('reserva/<int:pk>/', views.detalhes_reserva, name='detalhes_reserva'),
    path('reserva/nova/', views.nova_reserva, name='nova_reserva'),
    path('reserva/editar/<int:pk>/', views.editar_reserva, name='editar_reserva'),
    path('reserva/deletar/<int:pk>/', views.deletar_reserva, name='deletar_reserva'),

    # URLs para o modelo Log
    path('logs/', views.lista_logs, name='lista_logs'),
    path('log/<int:pk>/', views.detalhes_log, name='detalhes_log'),
    path('log/novo/', views.novo_log, name='novo_log'),
    path('log/editar/<int:pk>/', views.editar_log, name='editar_log'),
    path('log/deletar/<int:pk>/', views.deletar_log, name='deletar_log'),

    # As URLs para os outros modelos continuam aqui...
]
