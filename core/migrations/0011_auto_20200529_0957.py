# Generated by Django 3.0.6 on 2020-05-29 09:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(blank=True, default='avatar.jpg', upload_to='profile_pics'),
        ),
    ]
