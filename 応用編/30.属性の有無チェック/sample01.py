class AttrTest():

    def __init__(self):
        self.code = -1


attr_test = AttrTest()
attr_test.name = 'python-izm'

print(hasattr(attr_test, 'code'))
print(hasattr(attr_test, 'name'))
print(hasattr(attr_test, 'kana'))
