import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

print('Pythonの学習サイト : %s' % 'python-izm.com')
print('Pythonの学習サイト : %s-%s.%s' % ('python', 'izm', 'com'))

test_int = 100 + 100
test_str = 'python-izm.com'
print('サイト開設 %d 日目! %s' % (test_int, test_str))
