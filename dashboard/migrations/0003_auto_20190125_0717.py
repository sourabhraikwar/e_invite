# Generated by Django 2.1.5 on 2019-01-25 07:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0002_email_model_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='email_model',
            name='status',
            field=models.CharField(default='0', max_length=2),
        ),
    ]
