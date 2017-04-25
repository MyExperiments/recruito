# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-25 07:02
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('rms', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Recruiter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company', models.CharField(max_length=50, verbose_name='Company')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='RecruiterSector',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Sector')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.CharField(choices=[('recruiter', 'Recruiter'), ('candidate', 'Candidate')], max_length=25, verbose_name='Role')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='recruiter',
            name='sector',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rms.RecruiterSector'),
        ),
        migrations.AddField(
            model_name='job',
            name='recruiter',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='rms.Recruiter'),
            preserve_default=False,
        ),
    ]