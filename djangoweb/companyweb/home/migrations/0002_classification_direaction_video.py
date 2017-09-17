# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Classification',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('weight', models.IntegerField(default=0, verbose_name=b'\xe6\x9d\x83\xe9\x87\x8d')),
                ('name', models.CharField(max_length=30, verbose_name=b'\xe5\x90\x8d\xe7\xa7\xb0')),
            ],
            options={
                'db_table': 'Classification',
                'verbose_name': '\u5206\u7c7b',
                'verbose_name_plural': '\u5206\u7c7b',
            },
        ),
        migrations.CreateModel(
            name='Direaction',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('weight', models.IntegerField(default=0, verbose_name=b'\xe6\x9d\x83\xe9\x87\x8d')),
                ('name', models.CharField(max_length=32, verbose_name=b'\xe5\x90\x8d\xe7\xa7\xb0')),
                ('classification', models.ManyToManyField(to='home.Classification')),
            ],
            options={
                'db_table': 'Direction',
                'verbose_name': '\u65b9\u5411',
                'verbose_name_plural': '\u65b9\u5411',
            },
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('status', models.IntegerField(default=1, verbose_name=b'\xe7\x8a\xb6\xe6\x80\x81', choices=[(0, b'\xe4\xb8\x8b\xe7\xba\xbf'), (1, b'\xe4\xb8\x8a\xe7\xba\xbf')])),
                ('level', models.IntegerField(default=1, verbose_name=b'\xe7\xba\xa7\xe5\x88\xab', choices=[(1, b'\xe5\x88\x9d\xe7\xba\xa7'), (2, b'\xe4\xb8\xad\xe7\xba\xa7'), (3, b'\xe9\xab\x98\xe7\xba\xa7')])),
                ('weight', models.IntegerField(default=0, verbose_name=b'\xe6\x9d\x83\xe9\x87\x8d')),
                ('title', models.CharField(max_length=32, verbose_name=b'\xe6\xa0\x87\xe9\xa2\x98')),
                ('img', models.ImageField(upload_to=b'./static/images/Video', verbose_name=b'\xe5\x9b\xbe\xe7\x89\x87')),
                ('href', models.CharField(max_length=256, verbose_name=b'\xe8\xa7\x86\xe9\xa2\x91\xe5\x9c\xb0\xe5\x9d\x80')),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('classification', models.ForeignKey(blank=True, to='home.Classification', null=True)),
            ],
            options={
                'db_table': 'Video',
                'verbose_name': '\u89c6\u9891',
                'verbose_name_plural': '\u89c6\u9891',
            },
        ),
    ]
