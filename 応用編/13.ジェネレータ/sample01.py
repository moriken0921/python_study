import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

def func_sample():
    yield('おはよう')
    yield('こんにちは')
    yield('こんばんは')

#for i in func_sample():
#    print(i)

f = func_sample()
print(next(f))
print(next(f))
print(f.next())
