file = open('datafile.txt','r')

for line in file:
    line_split = line.split(';')
    if (line_split[0] == '2'):
        print(line_split[1])

file.close()
