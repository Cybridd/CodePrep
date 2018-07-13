# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-03-21 21:05
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, unique=True)),
                ('overview', models.TextField(max_length=1000)),
                ('courselink', models.URLField()),
                ('price', models.IntegerField(default=0)),
                ('slug', models.SlugField(unique=True)),
                ('rating', models.IntegerField(default=0, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='LearningStyle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='Provider',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, unique=True)),
                ('logolink', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.IntegerField(default=0, null=True)),
                ('comment', models.TextField(max_length=5000)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CodePrep.Course')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('website', models.URLField(blank=True)),
                ('picture', models.ImageField(blank=True, upload_to='profile_images')),
                ('enrolledcourses', models.ManyToManyField(to='CodePrep.Course')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='course',
            name='provider',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='CodePrep.Provider'),
        ),
        migrations.AddField(
            model_name='course',
            name='style',
            field=models.ManyToManyField(to='CodePrep.LearningStyle'),
        ),
        migrations.AddField(
            model_name='course',
            name='subject',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='CodePrep.Subject'),
        ),
    ]
