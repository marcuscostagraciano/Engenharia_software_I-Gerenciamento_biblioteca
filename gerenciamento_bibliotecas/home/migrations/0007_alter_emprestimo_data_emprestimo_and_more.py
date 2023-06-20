# Generated by Django 4.2.2 on 2023-06-20 13:56

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_emprestimo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emprestimo',
            name='data_emprestimo',
            field=models.DateField(default=datetime.date(2023, 6, 20)),
        ),
        migrations.AlterField(
            model_name='emprestimo',
            name='prazo_devolucao',
            field=models.DateField(default=datetime.date(2023, 8, 21)),
        ),
        migrations.AlterField(
            model_name='livro',
            name='categoria',
            field=models.CharField(choices=[('INFANTIL', 'Infantil'), ('JUVENIL', 'Juvenil'), ('ADULTO', 'Adulto')], max_length=10),
        ),
        migrations.AlterField(
            model_name='livro',
            name='genero',
            field=models.ManyToManyField(choices=[(1, 'Ensaio'), (4, 'Novela'), (2, 'Romance'), (3, 'Romance filosófico')], to='home.genero'),
        ),
        migrations.AlterField(
            model_name='livro',
            name='localizacao',
            field=models.CharField(choices=[('000', 'Generalidades'), ('100', 'Filosofia e Psicologia'), ('200', 'Religião'), ('300', 'Ciências sociais'), ('400', 'Língua e Linguagem'), ('500', 'Ciências Puras'), ('600', 'Tecnologia e ciências aplicadas'), ('700', 'Artes/Esportes e Recreação'), ('800', 'Literatura'), ('900', 'Geografia/História/Biografia')], max_length=3),
        ),
    ]
