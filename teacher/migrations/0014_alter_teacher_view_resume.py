# Generated by Django 4.1.7 on 2023-03-16 19:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0013_teacher_entrance_teacher_teaching_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='view_resume',
            field=models.FileField(blank=True, null=True, upload_to='CV', verbose_name='ارسال رزومه'),
        ),
    ]
