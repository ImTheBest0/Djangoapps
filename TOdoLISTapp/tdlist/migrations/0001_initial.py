# Generated by Django 4.1.4 on 2023-01-05 22:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tasks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('deadline', models.DateTimeField()),
                ('description', models.TextField()),
                ('status', models.BooleanField(default=False)),
            ],
        ),
    ]
