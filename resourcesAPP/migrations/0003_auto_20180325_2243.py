# Generated by Django 2.0.3 on 2018-03-25 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resourcesAPP', '0002_auto_20180325_2237'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='click',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='bookmark',
            name='click',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='topic',
            name='click',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
