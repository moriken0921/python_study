import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

print('あなたの名前を教えてください。')

your_name = input('>> ')

print(your_name)
