from threading import Thread,Lock
import time

g_num = 0

def test():
    global g_num
    for i in  range(100000):
        mutexFlag = mutex.acquire(True)
        if mutexFlag:
            g_num += 1
            mutex.release()

        print('----test -gnum %d' % g_num)

def test1():
    global g_num
    for i in  range(100000):
        mutexFlag = mutex.acquire(True)
        if mutexFlag:
            g_num += 1
            mutex.release()
        print('----test -gnum %d' % g_num)


mutex = Lock()

p1 = Thread(target=test)
p1.start()

p2 = Thread(target=test1)
p2.start()

print('g num = %d'% g_num)


