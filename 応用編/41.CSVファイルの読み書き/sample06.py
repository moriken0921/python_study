import csv

csv_file = open('/Users/kentomori/Documents/GitHub/python_study/応用編/41.CSVファイルの読み書き/python.csv', 'r', newline='')
reader = csv.reader(csv_file)

for row in reader:
    print('-------------------')
    for cell in row:
        print(cell)

csv_file.close()
