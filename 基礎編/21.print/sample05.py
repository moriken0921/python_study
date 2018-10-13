import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

print('Pythonの学習サイト : {}'.format('python-izm.com'))
print('Pythonの学習サイト : {0}-{1}.{2}'.format('python', 'izm', 'com'))

test_int = 100 + 100
test_str = 'python-izm.com'
print('サイト開設{1}日目！{0}'.format(test_str, test_int))
