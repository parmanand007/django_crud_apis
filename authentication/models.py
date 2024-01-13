from django.db import models
from django.core.validators import MaxLengthValidator, MinLengthValidator
import json
from django.core.exceptions import ValidationError
# Create your models here.
class Animal(models.Model):
    name = models.CharField(max_length=255, validators=[
        MaxLengthValidator(limit_value=255, message='Name must be at most 255 characters.'),
        MinLengthValidator(limit_value=1, message='Name must be at least 1 character.')
    ])
    type_choices = [('Herbivore', 'Herbivore'), ('Carnivore', 'Carnivore')]
    type = models.CharField(max_length=10, choices=type_choices)
    sound = models.CharField(max_length=255, validators=[
        MaxLengthValidator(limit_value=255, message='Sound must be at most 255 characters.'),
        MinLengthValidator(limit_value=1, message='Sound must be at least 1 character.')
    ])
    extra_information = models.JSONField()
    owner = models.ForeignKey('auth.User', related_name='animals', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-id']
        db_table = "crud_animal"
        
    def __str__(self):
        return self.name
    
    def clean(self):
        try:
            json_data = json.loads(self.extra_information)
        except json.JSONDecodeError:
            raise ValidationError({'extra_information': 'Invalid JSON format.'})

        # Save the sanitized JSON data back to the model
        self.extra_information = json.dumps(json_data)