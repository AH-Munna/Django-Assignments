# Generated by Django 4.0.2 on 2022-05-03 11:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_content', '0008_alter_quizmcq_quiz'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quiz',
            name='number_of_MCQs',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='quiz',
            name='total_marks',
            field=models.IntegerField(),
        ),
    ]