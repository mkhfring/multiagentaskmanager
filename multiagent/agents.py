import time


class Agent:
    def __init__(self, manager):
        self.task_index = 0
        self.manager = manager

    def add_agent_result_to_manager(self):
        self.manager.task_result[self.name] = {
            'current_task':None,
            'finished_tasks': list(),
            'progress':None
        }

    def consum_tasks(self):
        return NotImplemented


class Greeting(Agent):
    def __init__(self, manager):
        super().__init__(manager)
        self.name = 'Greeting'


    def consum_tasks(self):
        self.add_agent_result_to_manager()
        while self.task_index != len(self.manager.tasks):
            task = self.manager.tasks[self.task_index]
            self.manager.task_result[self.name]['current_task'] = task

            self.manager.task_result[self.name]
            print (f"hello {task}")
            self.manager.task_result[self.name]['finished_tasks'].append(task)
            self.task_index += 1
            time.sleep(1)


class Goodby(Agent):
    def __init__(self, manager):
        super().__init__(manager)
        self.name = 'Goodby'

    def consum_tasks(self):
        self.add_agent_result_to_manager()
        while self.task_index != len(self.manager.tasks):
            task = self.manager.tasks[self.task_index]
            self.manager.task_result[self.name]['current_task'] = task
            print (f"Goodby {task}")
            self.manager.task_result[self.name]['finished_tasks'].append(task)
            self.task_index += 1
            time.sleep(2)

