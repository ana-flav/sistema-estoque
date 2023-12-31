# Generated by Django 4.2.4 on 2023-08-02 22:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Funcionario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cpf', models.CharField(blank=True, max_length=11, null=True, unique=True, verbose_name='CPF')),
                ('nome', models.CharField(max_length=300, verbose_name='Nome')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='E-mail')),
                ('cargo', models.IntegerField(choices=[('1', 'Administrador'), ('2', 'Gerente'), ('3', 'Funcionário')], max_length=50, verbose_name='Cargo')),
                ('cod_trabalhador', models.IntegerField(blank=True, null=True, verbose_name='Código do Trabalhador')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Usuário')),
            ],
        ),
    ]
