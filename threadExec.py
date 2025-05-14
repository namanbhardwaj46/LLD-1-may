import time
import threading
from concurrent.futures.thread import ThreadPoolExecutor


def hello_world(t):
    time.sleep(t)
    return f"Hello world-name -  {threading.current_thread().name}"


time1 = time.perf_counter()

with ThreadPoolExecutor(max_workers=3) as executor:
    f1 = executor.submit(hello_world, 4) # w w w       w       printed
    print(f"f1 {f1.result()}")
    print("a")
    f2 = executor.submit(hello_world, 3)  # w w w       Printed
    f3 = executor.submit(hello_world, 2)  # q q q       w        w        Printed

    print(f"f2 {f2.result()}")
    print(f"f3 {f3.result()}")


time2 = time.perf_counter()

print(f"Execution time : {time2 - time1}")




# import time
# import threading
# import multiprocessing
# from concurrent.futures.process import ProcessPoolExecutor
#
#
#
# def hello_world(t):
#     time.sleep(t)
#     return f"Hello world-name -  {multiprocessing.current_process().name}"
#
#
# if __name__ == "__main__":
#
#
#     time1 = time.perf_counter()
#
#     with ProcessPoolExecutor(max_workers=3) as executor:
#         f1 = executor.submit(hello_world, 4) # w w w       w       printed
#         print(f"f1 {f1.result()}")
#         print("a")
#         executor.submit(hello_world, 3)  # w w w       Printed
#         executor.submit(hello_world, 2)  # q q q       w        w        Printed
#
#
#     time2 = time.perf_counter()
#
#     print(f"Execution time : {time2 - time1}")
