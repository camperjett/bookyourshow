# Generated by Django 3.2.9 on 2021-11-12 06:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0006_auto_20211112_1110'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='showdetail',
            name='duration',
        ),
    ]