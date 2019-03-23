class ContextManagerTest:

    def __enter__(self):
        print('__enter__')
        return 'as obj'

    def __exit__(self, exc_type, exc_value, traceback):
        print('__exit__')


with ContextManagerTest() as as_obj:
    print(as_obj)
