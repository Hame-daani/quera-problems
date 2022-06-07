from threading import currentThread
import time

_chf = [False, False, False, False]
_chg = [False, False]
_chh = [False]

def f(i):

    def _f():
        time.sleep(0.1)
        _chf[i-1] = (currentThread().getName() == str(i))

    return _f

def g(i):

    def _g():
        time.sleep(0.1)
        _chg[i-1] = (currentThread().getName() == str(i) and _chf[2*i-1] and _chf[2*i-2])

    return _g

def _h():
    time.sleep(0.1)
    _chh[0] = (currentThread().getName() == '1' and _chg[0] and _chg[1])

f = [f(1), f(2), f(3), f(4)]
g = [g(1), g(2)]
h = [_h]
