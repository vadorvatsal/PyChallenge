# install using pip excel2json-3


# Method 1
# import excel2json
# EXCEL_FILE = '/Users/Username/Desktop/Book1.xlsx'
# excel2json.convert_from_file(EXCEL_FILE)


# Method 2
import pandas
import json
#
excel_data_df = pandas.read_excel('/path/to/excel/file.xlsx', sheet_name='Sheet1')
json_str = excel_data_df.to_json(orient='records')
json_clean_str = json_str.replace("\'", '"')
json_clean_str = json_clean_str.replace("\/", "/")


with open('resultjson.json','w') as outfile:
    json.dump(json_clean_str, outfile, ensure_ascii=False, indent=4)
