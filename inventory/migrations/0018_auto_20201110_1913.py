# Generated by Django 3.1.2 on 2020-11-10 19:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0017_auto_20201102_1915'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='itemloan',
            name='returned_date',
        ),
        migrations.AlterField(
            model_name='itemloan',
            name='loan_to',
            field=models.DateField(verbose_name='Lån til'),
        ),
    ]
