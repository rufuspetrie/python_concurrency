from math import sqrt
import multiprocessing

class Consumer(multiprocessing.Process):
    def __init__(self, task_queue, result_queue):
        multiprocessing.Process.__init__(self)
        self.task_queue = task_queue
        self.result_queue = result_queue

    def run(self):
        pname = self.name
        while True:
            temp_task = self.task_queue.get()
            if temp_task is None:
                print(f"Exiting {pname}")
                self.task_queue.task_done()
                break
            print(f"{pname} processing task: {temp_task}")
            answer = temp_task.process()
            self.task_queue.task_done()
            self.result_queue.put(answer)

class Task():
    def __init__(self, x):
        self.x = x

    def process(self):
        if self.x < 2 or self.x == 2 or self.x == 0:
            return f"{self.x} is not a prime number"
        limit = int(sqrt(self.x)) + 1
        for i in range(3, limit, 2):
            if self.x % i == 0:
                return f"{self.x} is not a prime number"
        return f"{self.x} is a prime number"
    
    def __str__(self):
        return f"Checking whether {self.x} is prime"

if __name__ == "__main__":
    tasks = multiprocessing.JoinableQueue()
    results = multiprocessing.Queue()

    n_consumers = multiprocessing.cpu_count()
    print(f"Spawning {n_consumers} consumers...")
    consumers = [Consumer(tasks, results) for i in range(n_consumers)]
    for consumer in consumers:
        consumer.start()

    my_input = [2, 36, 101, 193, 323, 513, 1327, 100000, 9999999, 433785907]
    for item in my_input:
        tasks.put(Task(item))
    # Putting Nones in the queue and allowing the run method to handle them is known as Poison pilling
    # It should allow more different processors to work, can't get it going correctly though
    for i in range(n_consumers):
        tasks.put(None)
    tasks.join()

    for i in range(len(my_input)):
        temp_result = results.get()
        print("Result: ", temp_result)

    print("Done")