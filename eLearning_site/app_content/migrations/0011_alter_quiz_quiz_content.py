# Generated by Django 4.0.2 on 2022-05-03 11:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_content', '0010_remove_quiz_number_of_mcqs_quiz_quiz_content_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quiz',
            name='quiz_content',
            field=models.TextField(),
        ),
    ]
