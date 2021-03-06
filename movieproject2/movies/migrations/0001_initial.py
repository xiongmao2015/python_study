# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-24 12:03
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MovieInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('postid', models.IntegerField(verbose_name='电影号')),
                ('title', models.CharField(max_length=30, verbose_name='电影名')),
                ('image', models.CharField(max_length=100, verbose_name='电影宣传图')),
            ],
        ),
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=20, verbose_name='用户名')),
                ('password', models.CharField(max_length=60, verbose_name='密码')),
                ('mymovies', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movies.MovieInfo', verbose_name='我的收藏')),
            ],
        ),
    ]
