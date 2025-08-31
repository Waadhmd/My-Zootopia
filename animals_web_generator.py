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

def format_animals_text():
    animals = load_data(ANIMALS_DATA_FILENAME)
    output = ''
    for animal in animals:
        if 'name' in animal:
            output += f"Name: {animal['name']}\n"

        diet = animal.get('characteristics',{}).get('diet')
        if diet:
            output += f"Diet: {diet}\n"

        if 'locations' in animal:
            output += f"Location: {animal['locations'][0]}\n"

        animal_type_value = animal.get('characteristics',{}).get('type')
        if animal_type_value:
            output += f"Type: {animal_type_value}\n"
    return output

def main():
    animal_info_text = format_animals_text()
    html_template = load_html_template(TEMPLATE_FILENAME)
    rendered_html = html_template.replace('__REPLACE_ANIMALS_INFO__',animal_info_text)

    with open(OUTPUT_HTML_FILENAME , 'w') as output_file:
        output_file.write(rendered_html)

if __name__ == '__main__':
    main()
