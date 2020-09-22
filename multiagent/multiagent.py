from .agents import Greeting, Goodby


class MultiAgentTaskManager:

    def __init__(self, task_list):
        self.tasks = task_list
        self.agents = [Goodby(), Greeting()]

    def consum(self):
        for agent in self.agents:
            agent.consum_tasks(self.tasks)


    @property
    def get_agents(self):
        return self.agents

