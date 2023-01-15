import threading

class AdeasMessager(threading.Thread):
    def run(self):
        for _ in range(10):
            print(threading.current_thread().getName())
x = AdeasMessager(name= 'Send out messages')
y = AdeasMessager(name= 'Receive messages')
x.start()
y.start()