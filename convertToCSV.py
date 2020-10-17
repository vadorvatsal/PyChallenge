# Python program to convert
# JSON file to CSV


import json
import csv


# Opening JSON file and loading the data
# into the variable data
print("\nOpening json file . . .\n")
with open('data.json') as json_file:
    data = json.load(json_file)

print("\nFetching data . . .\n")
articles_data = data['articles']

# now we will open a file for writing
data_file = open('articles.csv', 'w')

# create the csv writer object
csv_writer = csv.writer(data_file)

# Counter variable used for writing
# headers to the CSV file
count = 0
print("\nCreating CSV file\n")
for article in articles_data:
    if count == 0:
        # Writing headers of CSV file
        header = article.keys()
        csv_writer.writerow(header)
        count += 1

    # Writing data of CSV file
    csv_writer.writerow(article.values())

data_file.close()
print("\nCompiled Successfully . . .\n")
