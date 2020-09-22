import os

import pytest

from multiagent import MultiAgentTaskManager, Greeting, Goodby


tasks =  ['Mohamad', 'Mehdi']

def test_multi_agent_manager():
    multiagent_task_manager = MultiAgentTaskManager(tasks)
    assert multiagent_task_manager.get_agents != None
    multiagent_task_manager.consum()

def test_agents():
    greeting = Greeting()
    greeting.consum_tasks(tasks)
    goodby = Goodby()
    goodby.consum_tasks(tasks)


