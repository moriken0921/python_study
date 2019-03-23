import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')


python_list = []
python_list.append('python')
python_list.append('izm')
python_list.append('sample')
python_list.append('list')
python_list.append('reversed')


print('---------------------------------')
print('【そのまま表示】')
for value in python_list:
    print(value)

print('---------------------------------')
print('【逆順表示】')
for value in reversed(python_list):
    print(value)

print('---------------------------------')
print('【リストの再表示】')
for value in python_list:
    print(value)
