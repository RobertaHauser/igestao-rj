# Generated by Django 3.0.2 on 2022-07-10 13:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_auto_20220710_1018'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='profile',
            options={'verbose_name': 'Perfil', 'verbose_name_plural': 'Perfis'},
        ),
        migrations.RemoveField(
            model_name='profile',
            name='profile',
        ),
        migrations.AddField(
            model_name='profile',
            name='perfil_name',
            field=models.CharField(blank=True, choices=[('MANAGER', 'Gerente'), ('ANALYST', 'Analista'), ('ASSISTANT', 'Assistente')], max_length=255, verbose_name='tipo'),
        ),
    ]
