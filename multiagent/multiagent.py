from threading import Thread
import asyncio

from .agents import Greeting, Goodby



class MultiAgentTaskManager:

    def __init__(self, task_list):
        self.tasks = task_list
        self.agents = [Goodby(self), Greeting(self)]
        self.task_result = {}

    def consum(self):
        loop = asyncio.get_event_loop()
        tasks = [
            loop.create_task(
                agent.consum_tasks()
            ) for agent in self.agents
        ]
        loop.run_until_complete(asyncio.gather(*tasks))
#            t = Thread(target=agent.consum_tasks)
#            t.start()

    @property
    def get_agents(self):
        return self.agents

    @property
    def get_task_result(self):
        return self.task_result

