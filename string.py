# my_string = "Hello World"
# substring = my_string[::-1]
# print(substring)

# greeting = "Hello"
# for x in greeting:
#     print(x)

# my_string = '   Hello World     '
# my_word = my_string.strip()
# print(my_word)

import functools
import datetime

def exception_catch(log_path):
    def deco(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except Exception as e:
                with open(log_path, 'a') as log:
                    log.write('{} {} {} {} {}\n'.format(datetime.datetime.now(), 
                                                        type(e), e, args, kwargs))
        return wrapper
    return deco