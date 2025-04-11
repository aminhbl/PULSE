import json
import csv

def csv_to_json(csv_file_path, json_output_path):
    data = []

    with open(csv_file_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            json_obj = {
                'file_name': row['Image name'] + '.png',
                'description': row['Description'],
                'label': row['Label'],
                # 'is_solved': row['Solved'].strip().lower() in ['true', '1', 'yes']
            }
            data.append(json_obj)

    with open(json_output_path, 'w', encoding='utf-8') as jsonfile:
        json.dump(data, jsonfile, ensure_ascii=False, indent=2)    

if __name__ == "__main__":
    csv_file = "Data/input_description.csv"
    output_file = "Data/input_description.json"

    csv_to_json(csv_file, output_file)
