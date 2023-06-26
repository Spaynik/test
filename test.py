import json

from jsonschema import validate, ValidationError

with open('schema.json', 'r') as f:
    schema = json.load(f)

with open('data.json', 'r') as f:
    data = json.load(f)

for item in data:
    try:
        validate(item, schema)
        print(f"JSON-данные валидны для {item['name']}")
    except ValidationError as e:
        print(f"JSON-данные невалидны для {item['name']}: {e.message}")
