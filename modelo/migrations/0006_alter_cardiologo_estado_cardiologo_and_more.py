# Generated by Django 4.0.4 on 2022-05-30 23:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('modelo', '0005_alter_cardiologo_estado_cardiologo_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cardiologo',
            name='estado_cardiologo',
            field=models.CharField(blank=True, default=None, max_length=100, verbose_name='estado_cardiologo'),
        ),
        migrations.AlterField(
            model_name='prequirurgico',
            name='estado_prequirurgico',
            field=models.CharField(blank=True, default=None, max_length=100, verbose_name='estado_prequirurgico'),
        ),
    ]
