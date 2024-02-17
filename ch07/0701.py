import multiprocessing

class ReductionConsumer(multiprocessing.Process):
    def __init__(self, task_queue, result_queue):
        multiprocessing.Process.__init__(self)
        self.task_queue = task_queue
        self.result_queue = result_queue

    def run(self):
        pname = self.name
        print(f"Using process {pname}...")

        while True:
            # First number is None - exit process
            num1 = self.task_queue.get()
            if num1 is None:
                print(f"Exiting process {pname}")
                self.task_queue.task_done()
                break
            # Second number is None - return first number
            self.task_queue.task_done()
            num2 = self.task_queue.get()
            if num2 is None:
                print(f"Reaching the end with process {pname} and {num1}")
                self.task_queue.task_done()
                self.result_queue.put(num1)
                break
            # Both exist - return sum
            print(f"Running process {pname} on numbers {num1} and {num2}")
            self.task_queue.task_done()
            self.result_queue.put(num1 + num2)

def reduce_sum(array):
    tasks = multiprocessing.JoinableQueue()
    results = multiprocessing.JoinableQueue()
    result_size = len(array)
    n_consumers = multiprocessing.cpu_count()
    
    for item in array:
        results.put(item)

    while result_size > 1:
        tasks = results
        results = multiprocessing.JoinableQueue()
        consumers = [ReductionConsumer(tasks, results) for i in range(n_consumers)]
        for consumer in consumers: 
            consumer.start()
        for i in range(n_consumers): 
            tasks.put(None)
        tasks.join()
        result_size = result_size // 2 + (result_size % 2)
        print("-" * 40)
    
    return results.get()

if __name__ == "__main__":
    my_array = [i for i in range(20)]
    result = reduce_sum(my_array)
    print(f"Final result: {result}")