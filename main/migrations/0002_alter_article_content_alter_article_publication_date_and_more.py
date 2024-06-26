# Generated by Django 5.0.6 on 2024-06-22 14:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='content',
            field=models.TextField(verbose_name='content'),
        ),
        migrations.AlterField(
            model_name='article',
            name='publication_date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='publication_date'),
        ),
        migrations.AlterField(
            model_name='article',
            name='title',
            field=models.CharField(max_length=255, verbose_name='title'),
        ),
    ]
