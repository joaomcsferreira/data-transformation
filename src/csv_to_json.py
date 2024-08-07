import csv
import json


def csv_to_json_object(csv_file_path, json_file_path):
    result = {}

    with open(csv_file_path, mode="r", encoding="utf-8") as csv_file:
        csv_reader = csv.DictReader(csv_file, delimiter=";")

        for row in csv_reader:
            nome = row["Nome"]
            result[nome] = row

    with open(json_file_path, mode="w", encoding="utf-8") as json_file:
        json.dump(result, json_file, indent=4, ensure_ascii=False)


csv_file_path = "csv/pi-fontes.csv"
json_file_path = "result/pi-fontes.json"
csv_to_json_object(csv_file_path, json_file_path)
