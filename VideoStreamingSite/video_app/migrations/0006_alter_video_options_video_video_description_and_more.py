# Generated by Django 4.0.2 on 2022-04-30 10:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('video_app', '0005_video_video_title'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='video',
            options={'ordering': ('-video_upload_date',)},
        ),
        migrations.AddField(
            model_name='video',
            name='video_description',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='video',
            name='video_title',
            field=models.CharField(default='title', max_length=264),
        ),
    ]
