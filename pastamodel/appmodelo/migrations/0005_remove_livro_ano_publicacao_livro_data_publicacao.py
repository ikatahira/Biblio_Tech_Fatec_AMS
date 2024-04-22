# Generated by Django 5.0.4 on 2024-04-20 03:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appmodelo', '0004_livro_descricao'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='livro',
            name='ano_publicacao',
        ),
        migrations.AddField(
            model_name='livro',
            name='data_publicacao',
            field=models.DateTimeField(auto_now_add=True, default='Descrição padrão'),
            preserve_default=False,
        ),
    ]