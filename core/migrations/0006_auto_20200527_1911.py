# Generated by Django 3.0.6 on 2020-05-27 19:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20200527_1819'),
    ]

    operations = [
        migrations.AddField(
            model_name='core',
            name='ingredients',
            field=models.ManyToManyField(to='core.Ingredient'),
        ),
        migrations.DeleteModel(
            name='RecipeIngredients',
        ),
    ]
