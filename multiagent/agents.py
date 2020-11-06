import time
import asyncio

import requests


class Agent:
    def __init__(self, manager, scanner_id):
        self.task_index = 0
        self.manager = manager
        self.scanner_id = scanner_id

    def add_agent_result_to_manager(self):
        self.manager.task_result[self.scanner_id] = {
            'current_task':None,
            'finished_tasks': list(),
            'progress':None
        }

    def consum_tasks(self):
        self.add_agent_result_to_manager()

        while self.task_index != len(self.manager.tasks):
            task = self.manager.tasks[self.task_index]
            scan_result = requests.post(
            'http://192.168.40.34:8081/api/v1/scanner/file',
            files={'file':open(task, 'rb')},
            data={'scanner_id': self.scanner_id},
            auth=('admin', 'admin')
            )
            self.manager.task_result[self.scanner_id]['current_task'] = \
                scan_result.json()['md5']
            self.task_index += 1

#        while self.task_index != len(self.manager.tasks):
#            task = self.manager.tasks[self.task_index]
#            self.manager.task_result[self.name]['current_task'] = task
#
#            self.manager.task_result[self.name]
#            print (f"{self.name} {task}")
#            self.manager.task_result[self.name]['finished_tasks'].append(task)
#            self.task_index += 1
#            if self.name == 'Hello':
#                time.sleep(1)
#            else:
#                time.sleep(2)


#class Greeting(Agent):
#    def __init__(self, manager):
#        super().__init__(manager)
#        self.name = 'Greeting'
#
#
#    async def consum_tasks(self):
#        self.add_agent_result_to_manager()
#        while self.task_index != len(self.manager.tasks):
#            task = self.manager.tasks[self.task_index]
#            self.manager.task_result[self.name]['current_task'] = task
#
#            self.manager.task_result[self.name]
#            print (f"hello {task}")
#            self.manager.task_result[self.name]['finished_tasks'].append(task)
#            self.task_index += 1
#            await asyncio.sleep(1)
#
#
#class Goodby(Agent):
#    def __init__(self, manager):
#        super().__init__(manager)
#        self.name = 'Goodby'
#
#    async def consum_tasks(self):
#        self.add_agent_result_to_manager()
#        while self.task_index != len(self.manager.tasks):
#            task = self.manager.tasks[self.task_index]
#            self.manager.task_result[self.name]['current_task'] = task
#            print (f"Goodby {task}")
#            self.manager.task_result[self.name]['finished_tasks'].append(task)
#            self.task_index += 1
#            await asyncio.sleep(2)
#
#
