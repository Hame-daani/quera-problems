import re
import functions
from threading import Thread


def calculate(i):
    try:
        functions.f[i - 1]()
        functions.g[i - 1]()
        functions.h[i - 1]()
        return
    except:
        return


def solve():
    t1 = Thread(target=calculate, args=(1,), name="1")
    t2 = Thread(target=calculate, args=(2,), name="2")
    t3 = Thread(target=calculate, args=(3,), name="3")
    t4 = Thread(target=calculate, args=(4,), name="4")
    t4.start()
    t3.start()
    t2.start()
    t1.start()
    t4.join()
    t3.join()
    t2.join()
    t1.join()
    return
