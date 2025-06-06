import threading
import  time

def hello_world(name):
    time.sleep(3)
    print(f"Hello world-name{name} -  {threading.current_thread().name}")


t1 = threading.Thread(target=hello_world, args=("Save to db",), name='t1')
t2 = threading.Thread(target=hello_world, args=("email",), name='t2')
t3 = threading.Thread(target=hello_world, args=("sms",), name='t3')
t1.start()

t1.join()

t2.start()
t3.start()
t2.join()
print("Main execution completed...")