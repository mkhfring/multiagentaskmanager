import os

import pytest
from celery import Celery

from multiagent import MultiAgentTaskManager, Greeting, Goodby


app = Celery('tests', backend='rpc://', brocker='pyamp://gust@localhost')
tasks =  ['mehdi', 'Mohamad', 'ghazal', 'alireza']

#def test_multi_agent_manager():
#    multiagent_task_manager = MultiAgentTaskManager(tasks)
#    assert multiagent_task_manager.get_agents != None
#    multiagent_task_manager.consum()
#    assert multiagent_task_manager.get_task_result is not None
#    assert 1 == 1


def test_agents():
    manager = MultiAgentTaskManager(tasks)
    greeting = Greeting(manager)
    greeting.delay()
    #app.tasks.register(Goodby(manager))
#    greeting = Greeting(manager)
#    greeting.delay()

#    goodby = Goodby(manager)
#    goodby.consum_tasks()


