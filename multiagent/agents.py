import time


class Agent:
    def __init__(self):
        self.task_index = 0

    def consum_tasks(self, task_list):
        return NotImplemented


class Greeting(Agent):
    def __init__(self):
        super().__init__()

    def consum_tasks(self, task_list):
        while self.task_index != len(task_list):
            task = task_list[self.task_index]
            print (f"hello {task}")
            self.task_index += 1
            time.sleep(1)


class Goodby(Agent):
    def __init__(self):
        super().__init__()

    def consum_tasks(self, task_list):
        while self.task_index != len(task_list):
            task = task_list[self.task_index]
            print (f"Goodby {task}")
            self.task_index += 1
            time.sleep(2)

