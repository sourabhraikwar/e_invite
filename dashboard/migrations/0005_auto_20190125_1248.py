# Generated by Django 2.1.5 on 2019-01-25 12:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0004_sendemails'),
    ]

    operations = [
        migrations.AlterField(
            model_name='email_model',
            name='status',
            field=models.CharField(default=1, max_length=2),
        ),
    ]
