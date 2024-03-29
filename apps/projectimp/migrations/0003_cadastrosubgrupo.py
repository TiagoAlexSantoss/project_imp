# Generated by Django 5.0.3 on 2024-03-27 14:03

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projectimp', '0002_cadastrogrupo'),
    ]

    operations = [
        migrations.CreateModel(
            name='CadastroSubGrupo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_subgrupo', models.CharField(max_length=200)),
                ('ordem_subgrupo', models.IntegerField(max_length=200)),
                ('ativo', models.BooleanField(default=False)),
                ('nome_grupo', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='user', to='projectimp.cadastrogrupo')),
            ],
        ),
    ]
