# Generated by Django 3.0.7 on 2020-08-10 23:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('link', '0007_auto_20200810_2356'),
    ]

    operations = [
        migrations.AlterField(
            model_name='url',
            name='short_url',
            field=models.CharField(max_length=20),
        ),
    ]
