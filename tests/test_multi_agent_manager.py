import os
import requests

import pytest

from multiagent import MultiAgentTaskManager


tasks =  ['tests/conftest.py', 'tests/test.txt']

def test_multi_agent_manager():
    multiagent_task_manager = MultiAgentTaskManager(tasks)
    assert multiagent_task_manager.get_agents != None
    multiagent_task_manager.consum()
    assert multiagent_task_manager.get_task_result is not None
    finished = multiagent_task_manager.tasks_are_finished()
    import pudb; pudb.set_trace()  # XXX BREAKPOINT
    assert 1 == 1


