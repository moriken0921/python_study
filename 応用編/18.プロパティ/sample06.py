class PropertyTest(object):

    def __init__(self, scheme, host):
        self.scheme = scheme
        self.host = host

    @property
    def url(self):
        return('{}://{}/'.format(self.scheme, self.host))


prop = PropertyTest('https', 'www.python-izm.com')

print(prop.url)
