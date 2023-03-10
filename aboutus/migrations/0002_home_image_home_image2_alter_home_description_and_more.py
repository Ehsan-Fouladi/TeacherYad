# Generated by Django 4.1.7 on 2023-03-10 22:37

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aboutus', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='home',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='about'),
        ),
        migrations.AddField(
            model_name='home',
            name='image2',
            field=models.ImageField(blank=True, null=True, upload_to='about'),
        ),
        migrations.AlterField(
            model_name='home',
            name='description',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='home',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='home',
            name='phone',
            field=models.CharField(blank=True, max_length=12, null=True),
        ),
        migrations.AlterField(
            model_name='home',
            name='subject',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='home',
            name='text',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='home',
            name='title',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
