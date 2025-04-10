# Generated by Django 5.1.5 on 2025-03-25 14:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Playlist',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('pf', models.CharField(max_length=1)),
                ('title', models.CharField(max_length=200)),
                ('visible', models.BooleanField()),
                ('desc', models.TextField()),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('thumbnail', models.ImageField(upload_to='playlist_thumbnail/')),
                ('slug', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('pf', models.CharField(max_length=1)),
                ('title', models.CharField(max_length=200)),
                ('visible', models.BooleanField()),
                ('desc', models.TextField()),
                ('thumbnail', models.ImageField(upload_to='video_thumbnail/')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('views', models.PositiveIntegerField()),
                ('likes', models.PositiveIntegerField()),
                ('slug', models.CharField(max_length=25)),
                ('source', models.CharField(max_length=300)),
            ],
        ),
    ]
