# Generated by Django 3.2.18 on 2023-04-11 19:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('applications', '0017_add_project_interests'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='project_interests',
            field=models.TextField(default='', verbose_name='Er det andre prosjekter du er interessert i?'),
        ),
    ]
