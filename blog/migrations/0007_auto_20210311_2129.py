# Generated by Django 3.1.7 on 2021-03-11 21:29

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_postimage'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='body',
        ),
        migrations.RemoveField(
            model_name='blog',
            name='img',
        ),
        migrations.AddField(
            model_name='blog',
            name='content',
            field=tinymce.models.HTMLField(default='SOME STRING'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='title',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
        migrations.DeleteModel(
            name='PostImage',
        ),
    ]
