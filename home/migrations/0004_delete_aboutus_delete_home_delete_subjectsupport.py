# Generated by Django 4.1.7 on 2023-02-21 21:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_aboutus_home_subjectsupport'),
    ]

    operations = [
        migrations.DeleteModel(
            name='AboutUs',
        ),
        migrations.DeleteModel(
            name='Home',
        ),
        migrations.DeleteModel(
            name='SubjectSupport',
        ),
    ]
