# Generated by Django 4.0.2 on 2022-05-03 10:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_content', '0007_remove_quiz_quiz_content_remove_quizmcq_teacher_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quizmcq',
            name='quiz',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='quiz_MCQs', to='app_content.quiz'),
        ),
    ]
