# Generated by Django 3.0.6 on 2020-05-28 13:55

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_auto_20200527_1911'),
    ]

    operations = [
        migrations.CreateModel(
            name='FoodGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group_name', models.CharField(max_length=200)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('published', models.DateField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.AlterField(
            model_name='core',
            name='category',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='core',
            name='cookTime',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='core',
            name='prepTime',
            field=models.CharField(max_length=20),
        ),
        migrations.DeleteModel(
            name='Group',
        ),
        migrations.AddField(
            model_name='foodgroup',
            name='recipe',
            field=models.ManyToManyField(to='core.Core'),
        ),
    ]
