import time


class Agent:
    def __init__(self):
        self.task_index = 0

    def consum_tasks(self):
        return NotImplemented


class Greeting(Agent):
    def __init__(self, manager):
        super().__init__()
        self.manager = manager


    def consum_tasks(self):
        while self.task_index != len(self.manager.tasks):
            task = self.manager.tasks[self.task_index]
            print (f"hello {task}")
            self.task_index += 1
            time.sleep(1)


class Goodby(Agent):
    def __init__(self, manager):
        super().__init__()
        self.manager = manager

    def consum_tasks(self):
        while self.task_index != len(self.manager.tasks):
            task = self.manager.tasks[self.task_index]
            print (f"Goodby {task}")
            self.task_index += 1
            time.sleep(2)

