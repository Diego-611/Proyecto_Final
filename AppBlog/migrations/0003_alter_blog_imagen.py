# Generated by Django 4.1 on 2022-10-08 21:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppBlog', '0002_rename_usuario_blog'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='imagen',
            field=models.ImageField(upload_to='fotos_blog'),
        ),
    ]