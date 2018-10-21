import os
import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')


filepath = '/Library/Frameworks/Python.framework/Versions/3.6/lib/python3.6'

if os.path.exists(filepath):
    print('指定のファイル、またはディレクトリが存在しています。')

    if os.path.isfile(filepath):
        print('指定のパスはファイルです。')

    if os.path.isdir(filepath):
        print('指定のパスはディレクトリです。')

else:
    print('指定のファイル、またはディレクトリが存在していません。')
