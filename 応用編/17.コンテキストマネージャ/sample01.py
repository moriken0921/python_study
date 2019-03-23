class ContextManagerTest:

    def __enter__(self):
        print('__enter__')

    def __exit__(self, exc_type, exc_value, traceback):
        print('__exit__')


with ContextManagerTest():
    print('with')
