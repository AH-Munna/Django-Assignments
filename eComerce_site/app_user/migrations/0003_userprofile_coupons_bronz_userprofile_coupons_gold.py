# Generated by Django 4.0.4 on 2022-05-13 10:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_user', '0002_user_account_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='coupons_bronz',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='coupons_gold',
            field=models.IntegerField(default=0),
        ),
    ]
