import os

import pytest

from multiagent import MultiAgentTaskManager, Greeting, Goodby


tasks =  ['mehdi', 'Mohamad', 'ghazal', 'alireza']

def test_multi_agent_manager():
    multiagent_task_manager = MultiAgentTaskManager(tasks)
    assert multiagent_task_manager.get_agents != None
    multiagent_task_manager.consum()
    assert multiagent_task_manager.get_task_result is not None
    assert 1 == 1


#def test_agents():
#    greeting = Greeting()
#    greeting.consum_tasks(tasks)
#    goodby = Goodby()
#    goodby.consum_tasks(tasks)


