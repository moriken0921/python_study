import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

f = open('/Users/kentomori/Documents/GitHub/python_study/応用編/14.ファイル読み書き/read.txt', 'r', encoding='utf-8')

for row in f:
    print(row)

f.close()
