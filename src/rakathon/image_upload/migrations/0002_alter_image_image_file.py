# Generated by Django 4.2.5 on 2023-09-07 08:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('image_upload', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='image_file',
            field=models.ImageField(upload_to=''),
        ),
    ]