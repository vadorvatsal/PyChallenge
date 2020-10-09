
# Method 1
from excel2json import convert_from_file
EXCEL_FILE = '/Users/vatsalvador/Desktop/interactiveChart.xlsx'
convert_from_file(EXCEL_FILE)


# Method 2
# import pandas
# import json
#
# excel_data_df = pandas.read_excel("/Users/vatsalvador/Desktop/interactiveChart.xlsx", sheet_name='Sheet1')
# json_str = excel_data_df.to_json(orient='records')
# json_str = json.dumps(json_str, ensure_ascii=False, indent=4)
# print("\n\n", json_str)

