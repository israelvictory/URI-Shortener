# Generated by Django 3.0.7 on 2020-08-10 22:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('link', '0003_auto_20200606_2214'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='url',
            name='short_url',
        ),
    ]