# Generated by Django 4.0.2 on 2022-05-02 11:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_account', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='accountprofile',
            old_name='name',
            new_name='acc_name',
        ),
    ]