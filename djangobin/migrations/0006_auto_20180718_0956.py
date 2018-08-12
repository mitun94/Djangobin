# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-07-18 09:56
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('djangobin', '0005_auto_20180718_0533'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='author',
            name='active',
        ),
        migrations.RemoveField(
            model_name='author',
            name='created_on',
        ),
        migrations.RemoveField(
            model_name='author',
            name='email',
        ),
        migrations.RemoveField(
            model_name='author',
            name='last_logged_in',
        ),
        migrations.RemoveField(
            model_name='author',
            name='name',
        ),
        migrations.AddField(
            model_name='author',
            name='default_expiration',
            field=models.CharField(choices=[('never', 'Never'), ('1 week', '1 week'), ('1 month', '1 month'), ('6 month', '6 month'), ('1 year', '1 year')], default='never', max_length=10),
        ),
        migrations.AddField(
            model_name='author',
            name='default_exposure',
            field=models.CharField(choices=[('public', 'Public'), ('unlisted', 'Unlisted'), ('private', 'Private')], default='public', max_length=10),
        ),
        migrations.AddField(
            model_name='author',
            name='default_language',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='djangobin.Language'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='author',
            name='private',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='author',
            name='user',
            field=models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='author',
            name='views',
            field=models.IntegerField(default=0),
        ),
    ]