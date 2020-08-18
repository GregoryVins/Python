import csv
import json

# Variable parameters
JSON_FILE = 'history.json'
CSV_FILE = 'result.csv'


def converter(f_json, f_csv):
    """
    Take a file in JSON format, read it and convert in CSV format
    :param f_json: JSON file when you need to read
    :param f_csv: CSV file when you need to write
    """
    with open(f_json)as json_file:
        DATA = json.load(json_file)

    with open(f_csv, 'w')as csv_file:
        writer = csv.writer(csv_file)
        for key, value in DATA.items():
            writer.writerow([key, value])
