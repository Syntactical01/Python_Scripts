# A decorator used to time methods
# from Fluent Python by Luciano Ramalho page 205.
import time
import functools

def clock(func):
    @functools.wraps(func)
    def clocked(*args, **kwargs):
        t0 = time.time()
        result = func(*args, **kwargs)
        elapsed = time.time() - t0
        name = func.__name__
        arg_list = []
        if args:
            arg_list.append(', '.join(repr(arg) for arg in args))
        if kwargs:
            pairs = ['{}={}'.format(k, w) for k, w in sorted(kwargs.items())]
            arg_list.append(','.join(pairs))
        arg_str = ', '.join(arg_list)
        print('[%0.8fs] %s(%s) -> %r ' % (elapsed, name, arg_str, result))
        return result
    return clocked

if __name__ == '__main__':
    @clock
    def sleep(sec):
        time.sleep(sec)
    sleep(sec=.123)
    sleep(1.24)
    
