# Generated by Django 2.1.3 on 2018-11-28 06:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_perro_estado'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='author',
        ),
        migrations.RemoveField(
            model_name='perro',
            name='color',
        ),
        migrations.DeleteModel(
            name='Post',
        ),
    ]
