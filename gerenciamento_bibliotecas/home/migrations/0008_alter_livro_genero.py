# Generated by Django 4.2.2 on 2023-06-20 14:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_alter_emprestimo_data_emprestimo_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='livro',
            name='genero',
            field=models.ManyToManyField(to='home.genero'),
        ),
    ]
