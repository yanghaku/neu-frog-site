# Generated by Django 2.0.3 on 2018-03-25 14:37

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('text', models.TextField()),
                ('created_time', models.DateTimeField(default=django.utils.timezone.now)),
                ('click', models.IntegerField(default=0)),
            ],
            options={
                'ordering': ['click', '-created_time'],
            },
        ),
        migrations.CreateModel(
            name='ArticleCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='BookCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='BookMark',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('url', models.URLField()),
                ('description', models.CharField(max_length=200)),
                ('created_time', models.DateField(default=django.utils.timezone.now)),
                ('click', models.IntegerField(default=0)),
                ('img', models.ImageField(blank=True, upload_to='bookmark_icon')),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='resourcesAPP.Article')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='resourcesAPP.BookCategory')),
            ],
            options={
                'ordering': ['click', '-created_time'],
            },
        ),
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, unique=True)),
                ('click', models.IntegerField(default=0)),
            ],
        ),
    ]
