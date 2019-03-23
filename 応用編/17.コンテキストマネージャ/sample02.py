class ContextManagerTest:

    def __enter__(self):
        print('__enter__')

    def __exit__(self, exc_type, exc_value, traceback):
        print('__exit__')
        print(exc_type)
        print(exc_value)
        print(traceback)
        return True


with ContextManagerTest():
    val = int('abc')
