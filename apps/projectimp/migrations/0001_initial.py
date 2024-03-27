# Generated by Django 5.0.3 on 2024-03-25 11:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='IdentificacaoEmpresa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_empresa', models.CharField(max_length=200)),
                ('email_empresa', models.EmailField(max_length=200)),
                ('fone_empresa', models.CharField(max_length=200)),
                ('cnpj_empresa', models.CharField(max_length=200)),
            ],
        ),
    ]