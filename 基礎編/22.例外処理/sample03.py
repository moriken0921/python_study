import sys
import io
import traceback
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

def exception_test(value_1, value_2):

    print('＝＝＝＝計算処理＝＝＝＝')

    result = 0

    try:
        result = value_1 + value_2
    except:
        print('計算出来ませんでした！')
        raise
    finally:
        print('計算終了')

    return result


try:
    print(exception_test(100, '200'))
except:
    print('---------------------------------------')
    print(traceback.format_exc(sys.exc_info()[2]))
    print('---------------------------------------')
