# Generated by Django 3.1.7 on 2021-03-16 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_remove_pokemon_veredito'),
    ]

    operations = [
        migrations.AddField(
            model_name='pokemon',
            name='veredito',
            field=models.BooleanField(default=True, editable=False),
        ),
    ]
