# Generated by Django 2.1.5 on 2019-02-13 10:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0008_auto_20190213_0659'),
    ]

    operations = [
        migrations.AlterField(
            model_name='createdvideos',
            name='output',
            field=models.FileField(blank=True, upload_to='uploads/%Y/%m/%d/output_file'),
        ),
    ]
