
# Method 1
from excel2json import convert_from_file
EXCEL_FILE = '/path/to/excel/file.xlsx'
convert_from_file(EXCEL_FILE)


# Method 2
# import pandas
# import json
#
# excel_data_df = pandas.read_excel('/path/to/excel/file.xlsx', sheet_name='Sheet1')
# json_str = excel_data_df.to_json(orient='records')
# json_str = json.dumps(json_str, ensure_ascii=False, indent=4)

