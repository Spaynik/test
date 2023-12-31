import json

from jsonschema import validate, ValidationError

with open('schema.json', 'r') as f:
    schema = json.load(f)

schema['properties']['name']['pattern'] = '^[A-Z][a-zA-Z0-9]*[0-9]$'
schema['properties']['name']['minLength'] = 3
schema['properties']['ip_address'] = {
    'type': 'string',
    'pattern': "^((25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.){3}(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])$"
}

with open('data.json', 'r') as f:
    data = json.load(f)

for i, item in enumerate(data):
    item["ip_address"] = f"192.168.1.{i + 1}"
    try:
        validate(item, schema)
        print(f"JSON-данные валидны после изменения для {item['name']}, IP: {item['ip_address']}")
    except ValidationError as e:
        print(f"JSON-данные невалидны после изменения для {item['name']}, IP: {item['ip_address']}: {e.message}")

with open("expressions.txt", "r") as file:
    expressions = file.readlines()

with open("result.html", "w", encoding='utf-8') as f:
    for vm in data:
        print(f"JSON-данные валидны для {vm['name']}")
        disk_sizes = vm['disk_sizes']
        for expr in expressions:
            result = eval(expr.strip())
            print(f"Выражение: {expr.strip()} для {vm['name']}")
            print(f"Результат: {result}")
            if expr.startswith('len(disk_sizes)'):
                f.write(f"<h1>{vm['name']}</h1>\n")
                f.write(f"<p>IP: {vm['ip_address']}, Количество дисков: {result}</p>\n")
