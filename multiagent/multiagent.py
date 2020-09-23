from threading import Thread
from multiagent.agents import Greeting, Goodby
from celery import Celery


tasks =  ['mehdi', 'Mohamad', 'ghazal', 'alireza']
app = Celery('agents', backend='rpc://', brocker='pyamp://gust@localhost', include=["tests"])

class MultiAgentTaskManager:

    def __init__(self, task_list):
        self.tasks = task_list
        self.agents = [Goodby(self), Greeting(self)]
        self.task_result = {}

    def consum(self):
        for agent in self.agents:
            t = Thread(target=agent.consum_tasks)
            t.start()


    @property
    def get_agents(self):
        return self.agents

    @property
    def get_task_result(self):
        return self.task_result

#print("!!!!!!!!!!!!!!")
manager = MultiAgentTaskManager(tasks)
app.tasks.register(Greeting(manager))
#greeting = Greeting(manager)
#greeting.delay()
