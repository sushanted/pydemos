from threading import Thread
from queue import Queue


# Simple multithreading

class CounterThread(Thread):

    def __init__(self, name):
        # Note this is important
        Thread.__init__(self)
        self.name = name

    def run(self):
        for i in range(10):
            print(self.name, i)


workers = []
for i in range(5):
    worker = CounterThread('thread' + str(i))
    worker.start()
    workers.append(worker)

# Wait for all threads
for worker in workers:
    worker.join()

print("\nMulti-threading using Queue\n")

# Using synchronous queue
q = Queue()
workers = []


def consume_items():
    while True:
        item = q.get()
        if not item:
            q.task_done()
            break
        print(item)
        # Somewhat like dynamic count-down latch (incr and decr till value becomes 0)
        q.task_done()


for i in range(5):
    worker = Thread(target=consume_items)
    worker.start()
    workers.append(worker)

# Produce items, though multiple workers working, the items will be consumed in FIFO order
for i in range(20):
    q.put(f'<item:{i}>')

# block until all tasks are done
q.join()

print("All tasks done!")

# Kill all workers feeding poison
for i in workers:
    # Poison
    q.put(None)

print("Killed all workers!")

# Wait for all workers to complete (die!)
for i in workers:
    i.join()

print("All workers dead!")
