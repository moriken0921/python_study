import sys

# 申し訳ございませんが、コマンドプロンプトで
# 呼び出したときに日本語printすると私の環境だとエラーでるので
# print内の文字を英語にしました。

args = sys.argv

print(args)
print('first argument:' + args[1])
print('second argument:' + args[2])
print('third argument:' + args[3])
