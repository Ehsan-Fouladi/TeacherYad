# Generated by Django 4.1.7 on 2023-02-21 21:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0011_alter_teacher_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='teacher',
            options={'ordering': ('-name_field',), 'verbose_name': 'مدرس', 'verbose_name_plural': 'معلم ها'},
        ),
    ]
