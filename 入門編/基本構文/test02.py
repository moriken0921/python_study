import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

print('モジュールのロード')

def test():
    print('関数：testを呼び出しました')

if __name__ == '__main__':

    print('python-izm')
#   print('パイソンイズム')
    test()
