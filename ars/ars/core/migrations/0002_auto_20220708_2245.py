# Generated by Django 3.0.2 on 2022-07-09 01:45

import ars.core.mixins
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='administrator',
            name='updated_at',
            field=ars.core.mixins.CustomDateTimeFieldCustom(auto_now=True, null=True, verbose_name='atualizado em'),
        ),
        migrations.AlterField(
            model_name='controller',
            name='updated_at',
            field=ars.core.mixins.CustomDateTimeFieldCustom(auto_now=True, null=True, verbose_name='atualizado em'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='updated_at',
            field=ars.core.mixins.CustomDateTimeFieldCustom(auto_now=True, null=True, verbose_name='atualizado em'),
        ),
        migrations.AlterField(
            model_name='provider',
            name='updated_at',
            field=ars.core.mixins.CustomDateTimeFieldCustom(auto_now=True, null=True, verbose_name='atualizado em'),
        ),
        migrations.AlterField(
            model_name='visitor',
            name='updated_at',
            field=ars.core.mixins.CustomDateTimeFieldCustom(auto_now=True, null=True, verbose_name='atualizado em'),
        ),
    ]