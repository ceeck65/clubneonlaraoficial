# Generated by Django 4.2.9 on 2024-11-28 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backoffice', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='birthday',
            field=models.DateField(blank=True, max_length=80, null=True),
        ),
    ]
