# Generated by Django 4.2.3 on 2023-07-14 10:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('uploader', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='uploadedfile',
            old_name='no_of_word',
            new_name='word_size',
        ),
    ]