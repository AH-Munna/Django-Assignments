# Generated by Django 4.0.2 on 2022-04-30 09:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('video_app', '0002_video_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='video_category',
            field=models.CharField(default='1', max_length=64),
        ),
    ]
