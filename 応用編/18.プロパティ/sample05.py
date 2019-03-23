class PropertyTest(object):

    def __init__(self, url):
        self._url = url

    @property
    def url(self):
        print('-- get_url --')
        return self._url

    @url.setter
    def url(self, url):
        print('-- set_url --')
        self._url = url

    @url.deleter
    def url(self):
        del self._url


prop = PropertyTest('https://www.python-izm.com/')

# setterにアクセス
prop.url = 'python-izm'

# getterにアクセス
print(prop.url)
