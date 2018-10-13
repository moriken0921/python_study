import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

# 関数
def test_func():
    print('call test_func')


class TestClass:
    # メソッド
    def test_method():
        print('call test_method')

print('------------------------')
print(test_func)
print(TestClass.test_method)

print('------------------------')
print(type(test_func))
print(type(TestClass.test_method))

print('------------------------')
t = TestClass()
print(test_func)
print(t.test_method)
