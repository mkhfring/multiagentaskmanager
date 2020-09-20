class MultiAgentTaskManager:

    def __init__(self, task_list):
        self.tasks = task_list
        self.agents = None

    def init_agents(self):
        return self.agents

    @property
    def get_agents(self):
        return 1


