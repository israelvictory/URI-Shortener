# Generated by Django 3.0 on 2020-06-06 21:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('link', '0002_url_visits'),
    ]

    operations = [
        migrations.RenameField(
            model_name='url',
            old_name='timestap',
            new_name='timestamp',
        ),
    ]
