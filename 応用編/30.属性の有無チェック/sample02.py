class AttrTest():

    def __init__(self):
        self.code = -1


attr_test = AttrTest()
attr_test.name = 'python-izm'

print(getattr(attr_test, 'code'))
print(getattr(attr_test, 'name'))
# print(getattr(attr_test, 'kana'))
print(getattr(attr_test, 'kana', 'No Attr'))
