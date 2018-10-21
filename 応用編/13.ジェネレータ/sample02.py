import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

gen_sample = (i for i in 'おはよう こんにちは こんばんは'.split())

print(gen_sample)
for i in gen_sample:
    print(i)
