# Generated by Django 3.1.8 on 2024-01-13 20:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('animal', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='animal',
            name='extra_information',
            field=models.JSONField(blank=True, default=dict),
        ),
    ]
