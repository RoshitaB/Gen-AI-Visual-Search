# Generated by Django 4.2.5 on 2023-09-07 08:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('image_upload', '0004_image_image_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='image_id',
            field=models.PositiveIntegerField(default=1, null=True),
        ),
    ]