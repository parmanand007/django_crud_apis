# import json
# from django.core.management.base import BaseCommand
# from django.contrib.auth.models import User
# from ...models import Animal

# class Command(BaseCommand):
#     help = 'Creates animals from a file and adds them to the database.'

#     def add_arguments(self, parser):
#         parser.add_argument('file_path', type=str, help='Path to the file containing the list of animals')
#         parser.add_argument('owner_username', type=str, help='Username of the owner')

#     def handle(self, *args, **kwargs):
#         file_path = kwargs['file_path']
#         owner_username = kwargs['owner_username']
#         print("===============>username",owner_username)
#         try:
#             owner = User.objects.get(username=owner_username)
#         except User.DoesNotExist:
#             self.stdout.write(self.style.ERROR(f"User with username '{owner_username}' does not exist."))
#             return

#         try:
#             with open(file_path, 'r') as file:
#                 animals_data = json.load(file)
#         except FileNotFoundError:
#             self.stdout.write(self.style.ERROR(f"File not found: '{file_path}'"))
#             return
#         except json.JSONDecodeError as e:
#             self.stdout.write(self.style.ERROR(f"Error decoding JSON in file '{file_path}': {e}"))
#             return

#         for animal_data in animals_data:
#             try:
#                 extra_information = json.dumps(animal_data.get('extra_information', {}))
#                 Animal.objects.create(
#                     name=animal_data['name'],
#                     type=animal_data['type'],
#                     sound=animal_data['sound'],
#                     owner=owner,
#                     extra_information=extra_information,
#                 )
#             except KeyError as e:
#                 self.stdout.write(self.style.ERROR(f"Missing required field in animal data: {e}"))
#                 return

#         self.stdout.write(self.style.SUCCESS(f"Animals from file '{file_path}' created successfully."))


from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from ...models import Animal
import json


class Command(BaseCommand):
    help = 'Creates animals from a file and adds them to the database.'

    def add_arguments(self, parser):
        parser.add_argument('file_path', type=str, help='Path to the file containing the list of animals')

    def handle(self, *args, **kwargs):
        file_path = kwargs['file_path']

        try:
            with open(file_path, 'r') as file:
                animals_data = json.load(file)
        except FileNotFoundError:
            self.stdout.write(self.style.ERROR(f"File not found: '{file_path}'"))
            return
        except json.JSONDecodeError as e:
            self.stdout.write(self.style.ERROR(f"Error decoding JSON in file '{file_path}': {e}"))
            return

        for animal_data in animals_data:
            try:
                owner_username = animal_data['owner']
                owner = User.objects.get(username=owner_username)

                extra_information = json.dumps(animal_data.get('extra_information', {}))

                Animal.objects.create(
                    name=animal_data['name'],
                    type=animal_data['type'],
                    sound=animal_data['sound'],
                    owner=owner,
                    extra_information=extra_information,
                )
            except KeyError as e:
                self.stdout.write(self.style.ERROR(f"Missing required field in animal data: {e}"))
                return
            except User.DoesNotExist:
                self.stdout.write(self.style.ERROR(f"User with username '{owner_username}' does not exist."))
                return

        self.stdout.write(self.style.SUCCESS(f"Animals from file '{file_path}' created successfully."))
