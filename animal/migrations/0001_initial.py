# Generated by Django 3.1.8 on 2024-01-13 15:34

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Animal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, validators=[django.core.validators.MaxLengthValidator(limit_value=255, message='Name must be at most 255 characters.'), django.core.validators.MinLengthValidator(limit_value=1, message='Name must be at least 1 character.')])),
                ('type', models.CharField(choices=[('Herbivore', 'Herbivore'), ('Carnivore', 'Carnivore')], max_length=10)),
                ('sound', models.CharField(max_length=255, validators=[django.core.validators.MaxLengthValidator(limit_value=255, message='Sound must be at most 255 characters.'), django.core.validators.MinLengthValidator(limit_value=1, message='Sound must be at least 1 character.')])),
                ('extra_information', models.JSONField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='animals', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'crud_animal',
                'ordering': ['-id'],
            },
        ),
    ]
