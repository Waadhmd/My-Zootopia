import json

ANIMALS_DATA_FILENAME = 'animals_data.json'

def load_data(file_path):
    with open(file_path , 'r') as handle:
        return json.load(handle)

def print_data():
    animals = load_data(ANIMALS_DATA_FILENAME)
    for animal in animals:
        print()
        if 'name' in animal:
            print(f"Name: {animal['name']}")

        diet = animal.get('characteristics',{}).get('diet')
        if diet:
            print(f"Diet: {diet}")

        if 'locations' in animal:
            print(f"Location: {animal['locations'][0]}")

        animal_type_value = animal.get('characteristics',{}).get('type')
        if animal_type_value:
            print(f"Type: {animal_type_value}")
print_data()

