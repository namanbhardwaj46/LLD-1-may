import threading

a = 0

mutex = threading.Lock()
mutex2 = threading.Lock()


def add():
    global a

    for i in range(10000000):
        print(1)
        mutex.acquire()

        a += 1
        mutex2.acquire()
        print("v")
        mutex2.release()
        mutex.release()


def sub():
    global a
    for i in range(10000000):
        mutex2.acquire()
        a -= 1
        mutex.acquire()
        mutex.release()
        mutex2.release()


t1 = threading.Thread(target=add)
t2 = threading.Thread(target=sub)

t1.start()
t2.start()

t1.join()
t2.join()

print(a)
