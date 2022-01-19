# Generated by Django 3.1.7 on 2022-01-19 20:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DoorStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datetime', models.DateTimeField()),
                ('status', models.BooleanField(default=False)),
                ('name', models.CharField(max_length=20)),
            ],
            options={
                'verbose_name_plural': 'Door Statuses',
            },
        ),
        migrations.CreateModel(
            name='OpenData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('opened', models.DateTimeField()),
                ('closed', models.DateTimeField()),
            ],
        ),
    ]
