import threading
import time

class MyThread(threading.Thread):
    def __init__(self, threadID, name, delay):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.delay = delay

    def run(self):
        print "Starting Thread: " + self.name
        print_time(self.name, self.delay, 5)
        print "Exiting: " + self.name


def print_time(name, delay, counter):
    while counter > 0:
        time.sleep(delay)
        print "%s: %s" % (name, time.ctime(time.time()))
        counter -= 1

# Create new Threads
myThread1 = MyThread(1, "t1", 2)
myThread2 = MyThread(2, "t2", 4)

# Start new Threads
myThread1.start()
myThread2.start()

print "Exiting main thread"
