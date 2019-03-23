from contextlib import contextmanager

@contextmanager
def context_manager_test():
    print('enter')
    yield 'as obj'
    print('exit')


with context_manager_test() as as_obj:
    print(as_obj)
