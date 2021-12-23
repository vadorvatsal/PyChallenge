import csv
import json

def csv_to_json(csvFilePath, jsonFilePath):
	jsonArray = []
	#read csv file
	with open(csvFilePath, encoding='utf-8') as csvf:
		csvReader = csv.DictReader(csvf)

		for row in csvReader:
			jsonArray.append(row)

	with open(jsonFilePath, 'w', encoding='utf-8') as jsonf:
		jsonString = json.dumps(jsonArray, indent=4)
		jsonf.write(jsonString)

csvFilePath = r'data.csv'
jsonFilePath = r'data.json'

csv_to_json(csvFilePath,jsonFilePath)