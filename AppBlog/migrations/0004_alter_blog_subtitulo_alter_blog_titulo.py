# Generated by Django 4.1 on 2022-10-10 18:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppBlog', '0003_alter_blog_imagen'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='subtitulo',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='blog',
            name='titulo',
            field=models.CharField(max_length=200),
        ),
    ]
