import time
import asyncio

import requests


class Agent:
    def __init__(self, manager, scanner_id, scanner_name):
        self.task_index = 0
        self.manager = manager
        self.scanner_id = scanner_id
        self.scanner_name = scanner_name

    def add_agent_result_to_manager(self):
        self.manager.task_result[self.scanner_name] = {
            'current_task':None,
            'finished_tasks': list(),
            'progress':None
        }

    def consum_tasks(self):
        self.add_agent_result_to_manager()

        while self.task_index != len(self.manager.tasks):
            task = self.manager.tasks[self.task_index]
            self.manager.task_result[self.scanner_name]['current_task'] = task
            scan_request = requests.post(
            'http://192.168.40.34:8081/api/v1/scanner/file',
            files={'file':open(task, 'rb')},
            data={'scanner_id': self.scanner_id},
            auth=('admin', 'admin')
            )
            while True:
                scan_result = requests.get(
                    'http://192.168.40.34:8081/api/v1/result/md5/{}/'.format(
                    scan_request.json()['md5']),
                    auth=('admin', 'admin')
                )
                if scan_result.status_code == 200:
                    break
                assert 1==1
            self.manager.task_result[self.scanner_name]['finished_tasks'].append(task)
            self.task_index += 1

        self.manager.number_of_finished_agents += 1
        assert 1 == 1

