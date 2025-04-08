import json
import csv
import os

def load_csv_data(csv_file):
    """Loads the CSV into a dictionary mapping file_name (without extension) to label/description."""
    csv_data = {}
    with open(csv_file, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            name = row["file_name"].strip()
            csv_data[name] = {
                "label": row.get("label", "").strip(),
                "description": row.get("description", "").strip()
            }
    return csv_data

def update_json_from_csv(json_file, csv_file, output_file=None):
    """Updates the JSON file's label and description using the CSV file."""
    with open(json_file, 'r', encoding='utf-8') as f:
        json_data = json.load(f)

    csv_data = load_csv_data(csv_file)

    updated_count = 0
    for item in json_data:
        base_name = os.path.splitext(item["file_name"])[0]
        if base_name in csv_data:
            if item["label"] == "" and csv_data[base_name]["label"]:
                item["label"] = csv_data[base_name]["label"]
            if item["description"] == "" and csv_data[base_name]["description"]:
                item["description"] = csv_data[base_name]["description"]
            updated_count += 1

    output_path = output_file or json_file  # Overwrite or save to a new file
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(json_data, f, indent=2)
    print(f"Updated {updated_count} entries and saved to {output_path}")

def main():
    json_file = "Data/ascii_logo_input_data.json"     # Input JSON file
    csv_file = "Data/input_description.csv"           # CSV with label/description
    output_file = "Data/ascii_output_updated.json"  # Optional: or overwrite json_file

    update_json_from_csv(json_file, csv_file, output_file)

if __name__ == "__main__":
    main()
