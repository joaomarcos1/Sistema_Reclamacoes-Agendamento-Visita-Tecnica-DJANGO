# Generated by Django 2.2.24 on 2021-12-08 00:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sistemaReclamacoes', '0011_atendimento'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='user',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]