# Generated by Django 4.0.6 on 2024-06-06 19:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LIG', '0006_projeto_nome'),
    ]

    operations = [
        migrations.AlterField(
            model_name='disciplina',
            name='docentes',
            field=models.ManyToManyField(blank=True, to='LIG.docente'),
        ),
    ]
