# Generated by Django 3.1.7 on 2021-03-19 18:42

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20210319_1827'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pokemonstrocados',
            name='pokemon_base_troca',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.TextField(editable=False, max_length=30, null=True), size=6),
        ),
        migrations.AlterField(
            model_name='pokemonstrocados',
            name='pokemon_base_user',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.TextField(editable=False, max_length=30, null=True), size=6),
        ),
        migrations.AlterField(
            model_name='pokemonstrocados',
            name='pokemon_img_troca',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.TextField(editable=False, max_length=30, null=True), size=6),
        ),
        migrations.AlterField(
            model_name='pokemonstrocados',
            name='pokemon_img_user',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.TextField(editable=False, max_length=30, null=True), size=6),
        ),
    ]