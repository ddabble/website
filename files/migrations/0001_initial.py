# Generated by Django 3.1.7 on 2022-01-19 20:23

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import files.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FileCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True, verbose_name='Kategori')),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Tittel')),
                ('time', models.DateTimeField(default=django.utils.timezone.now)),
                ('file', models.ImageField(upload_to='images')),
                ('thumb', models.ImageField(null=True, upload_to='thumbnails')),
                ('compressed', models.ImageField(null=True, upload_to='compressed')),
                ('number', models.IntegerField(default=0)),
                ('img_category', models.ForeignKey(default=files.models.get_default_category, on_delete=django.db.models.deletion.SET_DEFAULT, to='files.filecategory', verbose_name='Kategori')),
            ],
        ),
    ]
