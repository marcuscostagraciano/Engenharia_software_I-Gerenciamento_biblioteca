# Generated by Django 4.2.2 on 2023-06-20 00:59

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('home', '0005_livro_src_imagem'),
    ]

    operations = [
        migrations.CreateModel(
            name='Emprestimo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_emprestimo', models.DateField(default=datetime.date(2023, 6, 19))),
                ('prazo_devolucao', models.DateField(default=datetime.date(2023, 8, 20))),
                ('fk_livro', models.OneToOneField(on_delete=django.db.models.deletion.RESTRICT, to='home.livro')),
                ('fk_user', models.OneToOneField(on_delete=django.db.models.deletion.RESTRICT, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'emprestimo',
                'ordering': ['data_emprestimo'],
            },
        ),
    ]
