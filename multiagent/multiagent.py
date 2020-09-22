from threading import Thread
from .agents import Greeting, Goodby


class MultiAgentTaskManager:

    def __init__(self, task_list):
        self.tasks = task_list
        self.agents = [Goodby(self), Greeting(self)]

    def consum(self):
        for agent in self.agents:
            t = Thread(target=agent.consum_tasks)
            t.start()


    @property
    def get_agents(self):
        return self.agents

