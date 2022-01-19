# Generated by Django 3.1.7 on 2022-01-19 20:23

import ckeditor.fields
import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('files', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Banner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(default='Sample Text', help_text='Tekst som vises i banneret.', max_length=1000, verbose_name='bannertext')),
                ('color', models.CharField(default='hs-yellow', help_text='Bakgrunnsfargen til banneret som en hex-farge. hs-green, hs-yellow og hs-red støttes også som presets.', max_length=10, verbose_name='bannercolor')),
                ('text_color', models.CharField(default='hs-black', help_text='Tekstfargen på banneret. hs-white og hs-black støttes som presets.', max_length=10, verbose_name='bannertextcolor')),
                ('active', models.BooleanField(default=True, verbose_name='aktiv')),
                ('end_date', models.DateField(blank=True, default=datetime.datetime.now, help_text='Banneret vil ikke vises uansett om den har aktiv status etter denne datoen.', null=True, verbose_name='sluttdato')),
                ('site', models.CharField(default='*', help_text="Det interne navnet på URL-stien til sidene som banneret skal dukke opp på. Separert med komma (,). Wildcard (*) støttes. F.eks. er '*' ALLE sider, 'inventory:*' er alle lagersider.", max_length=250, verbose_name='bannersider')),
            ],
        ),
        migrations.CreateModel(
            name='FaqQuestion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=100, verbose_name='Spørsmål')),
                ('text', models.TextField(max_length=1000, verbose_name='Svar')),
                ('icon', models.CharField(help_text="Eksempel 'note_add' fra https://material.io/tools/icons/?style=baseline", max_length=30, verbose_name='Ikon')),
            ],
        ),
        migrations.CreateModel(
            name='Rule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Tittel')),
                ('body', ckeditor.fields.RichTextField()),
                ('internal', models.BooleanField(default=False, verbose_name='Intern regel')),
                ('printer_rule', models.BooleanField(default=False, verbose_name='Regel for bruk av printer')),
                ('priority', models.IntegerField(default=0)),
                ('thumb', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='files.image', verbose_name='Bilde')),
            ],
            options={
                'permissions': (('can_view_internal_rule', 'Can view internal rule'),),
            },
        ),
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Title')),
                ('body', models.TextField(max_length=200)),
                ('thumbnail_dark_text', models.BooleanField(default=False)),
                ('thumbnail', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='files.image')),
            ],
        ),
    ]
