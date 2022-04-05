from functools import wraps

def my_decorator_func(func):
    @wraps(func)
    def wrapper_func(*args, **kwargs):
        func(*args, **kwargs)
    return wrapper_func
@my_decorator_func
def my_func(my_args):
    '''Example doc string for function'''
    pass

print(my_func.__name__)
print(my_func.__doc__)