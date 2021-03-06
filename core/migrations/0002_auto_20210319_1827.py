# Generated by Django 3.1.7 on 2021-03-19 18:27

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pokemonstrocados',
            name='pokemon_base_troca',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.TextField(blank=True, editable=False, max_length=30), size=6),
        ),
        migrations.AlterField(
            model_name='pokemonstrocados',
            name='pokemon_base_user',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.TextField(blank=True, editable=False, max_length=30), size=6),
        ),
        migrations.AlterField(
            model_name='pokemonstrocados',
            name='pokemon_img_troca',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.TextField(blank=True, editable=False, max_length=30), size=6),
        ),
        migrations.AlterField(
            model_name='pokemonstrocados',
            name='pokemon_img_user',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.TextField(blank=True, editable=False, max_length=30), size=6),
        ),
    ]
