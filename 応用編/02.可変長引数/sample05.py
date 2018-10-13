import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

def test_func(code, name, kana, *args, **kwargs):
    print(code, name, kana)
    print(args)
    print(kwargs)

test_func(
    100, 'python-izm', u'パイソンイズム',
    'JP', 'US',
    email='xxxx', city='Tokyo'
)
