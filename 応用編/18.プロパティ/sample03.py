class PropertyTest(object):

    def __init__(self, scheme, host):
        self.schema = scheme
        self.host = host

    def get_url(self):
        return('{}://{}/'.format(self.schema, self.host))

    url = property(get_url)


prop = PropertyTest('https', 'www.python-izm.com')

print(prop.url)
