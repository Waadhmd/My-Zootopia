import json

ANIMALS_DATA_FILENAME = 'animals_data.json'
TEMPLATE_FILENAME = 'animals_template.html'
OUTPUT_HTML_FILENAME = "animals.html"

def load_data(file_path):
    with open(file_path , 'r') as handle:
        return json.load(handle)

def load_html_template(file_path):
    with open(file_path, 'r',encoding="utf-8") as template_file:
        return template_file.read()

def serialize_animal(animal:dict):
    output = ""

    output += '<li class="cards__item">'

    if 'name' in animal:
        output += f"<div class='card__title' > {animal['name']} </div>"
    output += '<p class="card__text">'
    diet = animal.get('characteristics', {}).get('diet')

    if diet:
        output += f"<strong>Diet:</strong>{diet} <br/>"

    if 'locations' in animal:
        output += f"<strong>Location:</strong>{animal['locations'][0]} <br/>"
    animal_type_value = animal.get('characteristics', {}).get('type')

    if animal_type_value:
        output += f"<strong>Type:</strong>{animal_type_value} <br/>"
    output += '</p>'
    output += '</li>'
    return output

def render_animals_text(animals:list):
    output = ''
    for animal in animals:
        output += serialize_animal(animal)
    return output

def main():
    animals = load_data(ANIMALS_DATA_FILENAME)
    animal_info_text = render_animals_text(animals)
    html_template = load_html_template(TEMPLATE_FILENAME)
    rendered_html = html_template.replace('__REPLACE_ANIMALS_INFO__',animal_info_text)

    with open(OUTPUT_HTML_FILENAME , 'w') as output_file:
        output_file.write(rendered_html)

if __name__ == '__main__':
    main()
