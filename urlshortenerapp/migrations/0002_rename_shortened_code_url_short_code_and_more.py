# Generated by Django 4.2.10 on 2024-02-29 05:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('urlshortenerapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='url',
            old_name='shortened_code',
            new_name='short_code',
        ),
        migrations.RemoveField(
            model_name='url',
            name='created_at',
        ),
    ]