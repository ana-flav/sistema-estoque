# Generated by Django 4.2.4 on 2023-08-03 12:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('funcionario', '0003_alter_funcionario_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='funcionario',
            name='cargo',
            field=models.IntegerField(choices=[(1, 'Administrador'), (1, 'Gerente'), (3, 'Funcionário')], verbose_name='Cargo'),
        ),
    ]
