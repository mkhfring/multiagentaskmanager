import os

import pytest

from multiagent import MultiAgentTaskManager


tasks =  ['Mohamad', 'Mehdi']

def test_multi_agent_manager():
    multiagent_task_manager = MultiAgentTaskManager(tasks)
    multiagent_task_manager.init_agents()
    assert multiagent_task_manager.get_agents != None

