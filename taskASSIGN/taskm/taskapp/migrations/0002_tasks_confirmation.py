# Generated by Django 4.1.4 on 2023-01-29 12:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taskapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tasks',
            name='confirmation',
            field=models.BooleanField(blank=True, null=True),
        ),
    ]
