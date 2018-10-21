fin_sjis = open('read.txt', 'r', encoding='shift_jis')
fout_euc = open('euc-jp.txt', 'w', encoding='euc_jp')
fout_utf = open('utf-8.txt', 'w', encoding='utf-8')

for row in fin_sjis:
    fout_euc.write(row)
    fout_utf.write(row)

fin_sjis.close()
fout_euc.close()
fout_utf.close()
