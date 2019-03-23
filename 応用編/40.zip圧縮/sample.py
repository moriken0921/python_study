test

Python-izm
Python の入門から応用までをサポートする学習サイト

TOP応用編
zip圧縮
Pythonの標準ライブラリでzip圧縮することができます。
※ここではデータ圧縮についてのzipを説明しています。複数の反復可能オブジェクトを同時に処理するzip関数、zip_longest関数はリンク先を参照してください。

zipfile

まずは圧縮対象のファイルを用意します。空のファイルでなければどのようなものでも構いませんので、下記ファイル名にて3つのファイルを作業ディレクトリに用意してください。

python.py
python.txt
python.csv
zip圧縮を行う例は次の通りです。

1
2
3
4
5
6
7
8
9
10
11
12
13
import zipfile

zipFile = zipfile.ZipFile('./compress_1.zip', 'w', zipfile.ZIP_STORED)
zipFile.write('./python.py')
zipFile.write('./python.txt')
zipFile.write('./python.csv')
zipFile.close()

zipFile = zipfile.ZipFile('./compress_2.zip', 'w', zipfile.ZIP_DEFLATED)
zipFile.write('./python.py')
zipFile.write('./python.txt')
zipFile.write('./python.csv')
zipFile.close()
 

Pythonのzip圧縮には複数のモードがあります。3行目で指定されているZIP_STOREDは複数のファイルをまとめるのみで、ファイルサイズ自体の圧縮は行いません。9行目のZIP_DEFLATEDではファイルサイズも圧縮されます。

1
2
3
4
5
6
7
8
9
10
11
12
13
import zipfile

zipFile = zipfile.ZipFile('./compress_1.zip', 'w', zipfile.ZIP_STORED)
zipFile.write('./python.py')
zipFile.write('./python.txt')
zipFile.write('./python.csv')
zipFile.close()

zipFile = zipfile.ZipFile('./compress_2.zip', 'w', zipfile.ZIP_DEFLATED)
zipFile.write('./python.py')
zipFile.write('./python.txt')
zipFile.write('./python.csv')
zipFile.close()
 

下記ハイライト部分で圧縮対象ファイルの追加を行っています。追加後はZipFileインスタンスをクローズして終了となります。出力されたファイルのサイズを見ると、モードの差が良く分かると思いますので確認してみてください。

1
2
3
4
5
6
7
8
9
10
11
12
13
import zipfile

zipFile = zipfile.ZipFile('./compress_1.zip', 'w', zipfile.ZIP_STORED)
zipFile.write('./python.py')
zipFile.write('./python.txt')
zipFile.write('./python.csv')
zipFile.close()

zipFile = zipfile.ZipFile('./compress_2.zip', 'w', zipfile.ZIP_DEFLATED)
zipFile.write('./python.py')
zipFile.write('./python.txt')
zipFile.write('./python.csv')
zipFile.close()
0
0
0
0
1








CSVファイルの読み書き
乱数値の取得
本サイトについて
プライバシーポリシー
お問い合わせ
目次（コンテンツ一覧）
総コンテンツ数 158 件
カテゴリー別

入門編 (8)
基礎編 (22)
応用編 (49)
豆知識 (10)
サードパーティ (21)
PDF (1)
画像処理 (1)
実行形式変換 (1)
データベース (3)
Excel操作 (8)
OpenPyXL (2)
python-excel (2)
XlsxWriter (1)
バージョン差吸収 (1)
データ解析 (11)
数値解析 (10)
NumPy (9)
Web (10)
CGI (1)
WSGI (2)
Django (4)
GUI (23)
wxPython (22)
教材 (4)
動画 (3)
Udemy (2)
P R


P R


P R


P R


入門編 基礎編 応用編 豆知識 サードパーティ Web GUI データ解析 教材
Copyright© Python-izm All Rights Reserved.
