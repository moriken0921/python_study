import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

import configparser


inifile = configparser.ConfigParser()
inifile.read('/Users/kentomori/Documents/GitHub/python_study/応用編/19.設定ファイル/config.ini', 'UTF-8')

print(inifile.get('ユーザー', 'name'))
print(inifile.get('ユーザー', 'name_kana'))
print(inifile.get('ユーザー', '備考'))
