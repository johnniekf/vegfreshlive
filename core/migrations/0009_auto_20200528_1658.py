# Generated by Django 3.0.6 on 2020-05-28 16:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_core_thumb'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='foodgroup',
            options={'ordering': ['-published']},
        ),
    ]
