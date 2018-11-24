# zad5   ###########################################
# zaimplementować prosty problem pieciu filozofow(z deadlockiem),
# nastepnie usunac deadlock
#####################################################
import sys
import threading
import time


class Semaphore(object):

    def __init__(self, initial):
        self.lock = threading.Condition(threading.Lock())
        self.value = initial

    def up(self):
        with self.lock:
            self.value += 1
            self.lock.notify()

    def down(self):
        with self.lock:
            while self.value == 0:
                self.lock.wait()
            self.value -= 1

class Fork(object):

    def __init__(self, fork_id):
        self.fork_id = fork_id
        self.user = -1
        self.lock = threading.Condition(threading.Lock())
        self.taken = False

    def take(self, user):
        with self.lock:
            while self.taken == True:
                self.lock.wait()
            self.user = user
            self.taken = True
            print("Philosoph {} took {} fork.\n".format(user, self.fork_id))
            self.lock.notifyAll()

    def drop(self, user):
        with self.lock:
            while self.taken == False:
                self.lock.wait()
            self.user = -1
            self.taken = False
            print("Philospoh {} dropped {} fork.\n".format(user, self.fork_id))
            self.lock.notifyAll()


class Philosopher (threading.Thread):

    def __init__(self, philosopher_id, left_fork, right_fork, butler):
        threading.Thread.__init__(self)
        self.philosopher_id = philosopher_id
        self.left_fork = left_fork
        self.right_fork = right_fork
        self.butler = butler

    def run(self):
        for i in range(20):
            self.butler.down()
            print("Philosopher {} is thinking.".format(self.philosopher_id))
            time.sleep(0.1)
            self.left_fork.take(self.philosopher_id)
            print("Philosopher {} is thinking.".format(self.philosopher_id))
            time.sleep(0.1)
            self.right_fork.take(self.philosopher_id)
            print("Philosopher {} is thinking.".format(self.philosopher_id))
            time.sleep(0.1)
            self.right_fork.drop(self.philosopher_id)
            self.left_fork.drop(self.philosopher_id)
            self.butler.up()
        sys.stdout.write("Philosopher {} finished thinking and eating\n".format(self.philosopher_id))

philosophers_amount = 5

butler = Semaphore(philosophers_amount - 1)
c = [Fork(i) for i in range(philosophers_amount)] 
p = [Philosopher(i, c[i], c[(i+1) % philosophers_amount], butler) for i in range(philosophers_amount)]

for i in range(philosophers_amount):
    p[i].start()
