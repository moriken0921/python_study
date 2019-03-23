from contextlib import contextmanager

@contextmanager
def context_manager_test():
    print('enter')
    yield
    print('exit')


with context_manager_test():
    print('with')
