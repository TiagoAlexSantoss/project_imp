# Generated by Django 5.0.3 on 2024-03-28 12:48

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projectimp', '0004_alter_cadastrogrupo_ordem_grupo_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='CadastroRespostaItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('resposta_item', models.CharField(max_length=200)),
                ('nome_item', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='nome_item_resp', to='projectimp.cadastroitem')),
            ],
        ),
    ]
