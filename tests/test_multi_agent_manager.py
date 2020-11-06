import os
import requests

import pytest

from multiagent import MultiAgentTaskManager


tasks =  ['tests/conftest.py', 'tests/test.txt']
#assert 1 == 1
#scan_result = requests.post(
#    'http://192.168.40.34:8081/api/v1/scanner/file',
#    files={'file':open(tasks[1], 'rb')},
#    data={'scanner_id': scanners_id[0]},
#    auth=('admin', 'admin')
#)
#import pudb; pudb.set_trace()  # XXX BREAKPOINT
#assert 1 == 1
#request = requests.get('http://192.168.40.34:8081/api/v1/result/md5/{}/'.format(scan_result.json()['md5']), auth=('admin', 'admin'))

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


