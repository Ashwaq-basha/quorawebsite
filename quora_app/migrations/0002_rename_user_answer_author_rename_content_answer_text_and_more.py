# Generated by Django 4.2.2 on 2023-06-12 10:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quora_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='answer',
            old_name='user',
            new_name='author',
        ),
        migrations.RenameField(
            model_name='answer',
            old_name='content',
            new_name='text',
        ),
        migrations.RenameField(
            model_name='question',
            old_name='user',
            new_name='author',
        ),
        migrations.RenameField(
            model_name='question',
            old_name='content',
            new_name='description',
        ),
    ]
