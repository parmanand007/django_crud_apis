from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from ...models import Animal
import json

class Command(BaseCommand):
    help = 'Creates a new animal entry in the database.'

    def add_arguments(self, parser):
        parser.add_argument('name', type=str, help='Name of the animal')
        parser.add_argument('type', type=str, choices=['Herbivore', 'Carnivore'], help='Type of the animal')
        parser.add_argument('sound', type=str, help='Sound the animal makes')
        parser.add_argument('owner_username', type=str, help='Username of the owner')
        parser.add_argument('--extra_information', type=str, help='Extra information in JSON format', default='{}')

    def handle(self, *args, **kwargs):
        name = kwargs['name']
        animal_type = kwargs['type']
        sound = kwargs['sound']
        owner_username = kwargs['owner_username']
        extra_information_str = kwargs['extra_information']

        try:
            owner = User.objects.get(username=owner_username)
        except User.DoesNotExist:
            self.stdout.write(self.style.ERROR(f"User with username '{owner_username}' does not exist."))
            return

        try:
            extra_information_dict = json.loads(extra_information_str)
            if not isinstance(extra_information_dict, dict):
                raise json.JSONDecodeError("Invalid JSON format for 'extra_information'.", extra_information_str, 0)
        except json.JSONDecodeError as e:
            self.stdout.write(self.style.ERROR(str(e)))
            return

        # Convert the extra_information_dict to a JSON string
        extra_information_json = json.dumps(extra_information_dict)

        animal = Animal.objects.create(
            name=name,
            type=animal_type,
            sound=sound,
            owner=owner,
            extra_information=extra_information_json,
        )

        self.stdout.write(self.style.SUCCESS(f"Animal '{animal.name}' created successfully."))
