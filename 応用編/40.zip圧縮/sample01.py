import zipfile

zipFile = zipfile.ZipFile('/Users/kentomori/Documents/GitHub/python_study/応用編/40.zip圧縮/compress_1.zip', 'w', zipfile.ZIP_STORED)
zipFile.write('/Users/kentomori/Documents/GitHub/python_study/応用編/40.zip圧縮/sample.py')
zipFile.write('/Users/kentomori/Documents/GitHub/python_study/応用編/40.zip圧縮/sample.txt')
zipFile.write('/Users/kentomori/Documents/GitHub/python_study/応用編/40.zip圧縮/sample.csv')
zipFile.close()

zipFile = zipfile.ZipFile('/Users/kentomori/Documents/GitHub/python_study/応用編/40.zip圧縮/compress_2.zip', 'w', zipfile.ZIP_DEFLATED)
zipFile.write('/Users/kentomori/Documents/GitHub/python_study/応用編/40.zip圧縮/sample.py')
zipFile.write('/Users/kentomori/Documents/GitHub/python_study/応用編/40.zip圧縮/sample.txt')
zipFile.write('/Users/kentomori/Documents/GitHub/python_study/応用編/40.zip圧縮/sample.csv')
zipFile.close()
