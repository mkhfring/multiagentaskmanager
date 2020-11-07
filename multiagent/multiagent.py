from threading import Thread
import asyncio

import requests

from .agents import Agent





class MultiAgentTaskManager:

    def __init__(self, task_list):
        response = requests.get(
            'http://192.168.40.34:8081/api/v1/scanners',
            auth=('admin', 'admin')
        )
        self.scanners = [(item['id'], item['name']) for item in response.json()]
        self.tasks = task_list
        self.agents = [
            Agent(self, scanner[0], scanner[1]) for scanner in self.scanners
        ]
        self.task_result = {}
        self.number_of_finished_agents = 0

    def consum(self):
#        loop = asyncio.get_event_loop()
#        tasks = [
#            loop.create_task(
#                agent.consum_tasks()
#            ) for agent in self.agents
#        ]
#        loop.run_until_complete(asyncio.gather(*tasks))
        for agent in self.agents:
#            agent.consum_tasks()
            t = Thread(target=agent.consum_tasks, daemon=True)
            t.start()

    @property
    def get_agents(self):
        return self.agents

    @property
    def get_task_result(self):
        return self.task_result

    def tasks_are_finished(self):
        return self.number_of_finished_agents == len(self.agents)

