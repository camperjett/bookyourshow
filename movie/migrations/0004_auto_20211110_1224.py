# Generated by Django 3.2.9 on 2021-11-10 06:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0003_alter_moviedetail_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='moviedetail',
            name='budget',
            field=models.DecimalField(decimal_places=2, max_digits=15),
        ),
        migrations.AlterField(
            model_name='moviedetail',
            name='director',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='moviedetail',
            name='genre',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='moviedetail',
            name='language',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='moviedetail',
            name='producer',
            field=models.CharField(max_length=50),
        ),
    ]