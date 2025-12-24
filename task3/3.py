import sys
import json

def open_file(file):
    with open(file, 'r') as f:
        return json.load(f)

def fill_values(data, result):
    if isinstance(data, dict):
        if 'id' in data and data['id'] in result:
            data['value'] = result[data['id']]

        for key in data:
            if isinstance(data[key], (dict, list)):
                fill_values(data[key], result)

    elif isinstance(data, list):
        for el in data:
            fill_values(el, result)

args_count = len(sys.argv)

if args_count != 4:
    print("Ошибка. Требуются аргументы: values.json tests.json report.json")
    sys.exit(1)

values_file = sys.argv[1]
tests_file = sys.argv[2]
report_file = sys.argv[3]

values_data = open_file(values_file)
tests_data = open_file(tests_file)

result = {}
for el in values_data['values']:
    result[el['id']] = el['value']

report_data = json.loads(json.dumps(tests_data))

fill_values(report_data, result)

with open(report_file, 'w') as f:
    json.dump(report_data, f, indent=2, ensure_ascii=False)

print(f"Отчет сохранен в {report_file}")
