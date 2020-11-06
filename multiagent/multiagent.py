from threading import Thread
import asyncio

import requests

from .agents import Agent


response = requests.get(
    'http://192.168.40.34:8081/api/v1/scanners',
    auth=('admin', 'admin')
)
scanners_id = [item['id'] for item in response.json()]



class MultiAgentTaskManager:

    def __init__(self, task_list):
        self.tasks = task_list
        self.agents = [Agent(self, scanner_id) for scanner_id in scanners_id]
        self.task_result = {}

    def consum(self):
#        loop = asyncio.get_event_loop()
#        tasks = [
#            loop.create_task(
#                agent.consum_tasks()
#            ) for agent in self.agents
#        ]
#        loop.run_until_complete(asyncio.gather(*tasks))
        for agent in self.agents:
            t = Thread(target=agent.consum_tasks)
            t.start()

    @property
    def get_agents(self):
        return self.agents

    @property
    def get_task_result(self):
        return self.task_result

