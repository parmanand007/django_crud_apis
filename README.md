

python manage.py create_animal Lion Carnivore Roar test --extra_information '{\"color\": \"golden\", \"weight\": \"200\"}'


python manage.py create_animals_from_file D:\New folder\crud_api\animal\animal_file.json --owner_username test


error: unrecognized arguments: --owner_username 

python manage.py create_animals_from_file "D:\New folder\crud_api\animal\animal_file.json" --owner_username "test"
