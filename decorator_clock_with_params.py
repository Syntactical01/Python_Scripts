# A decorator used to time methods
# from Fluent Python by Luciano Ramalho page 216.
# Note that this version cannot handle kargs (keyword arguments).
import time
DEFAULT_FMT = '[{elapsed:0.8f}s] {name}({args}) -> {result}'

def clock(fmt=DEFAULT_FMT):
    def decorate(func):
        def clocked(*_args):
            t0 = time.time()
            _result = func(*_args)
            elapsed = time.time() - t0
            name = func.__name__
            args = ', '.join(repr(arg) for arg in _args)
            result = repr(_result)
            # uses local variables for the format
            print(fmt.format(**locals()))
            return _result
        return clocked
    return decorate
if __name__ == '__main__':
    @clock('{name}: {elapsed}s')
    def snooze(seconds):
        time.sleep(seconds)
    for i in range(3):
        snooze(.123)
