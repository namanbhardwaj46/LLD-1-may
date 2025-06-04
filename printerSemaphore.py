import threading
import time

print_semaphore = threading.Semaphore(3)


def printDoc(user):
    # print(f"Document requested to be printed by {user}.")
    print_semaphore.acquire()
    print_semaphore.acquire()
    print(f"{user} is printing a document.")
    time.sleep(5)
    print(f"{user} finished printing.")

    print_semaphore.release()


def printDocWithBlock(user):
    # print(f"Document requested to be printed by {user}.")
    with print_semaphore:
        print(f"{user} is printing a document.")
        time.sleep(5)
        print(f"{user} finished printing.")






if __name__ == '__main__':
    users = ["User1", "User2", "User3", "User4", "User5", "User6", "User7", "User8", "User9", "User10"]

    threads = []
    for u in users:
        t = threading.Thread(target=printDocWithBlock, args=(u,))
        t.start()
        threads.append(t)


    for t in threads:
        t.join()