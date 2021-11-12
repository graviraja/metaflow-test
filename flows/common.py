import time
import subprocess
from importlib import import_module



def system_command_with_retry(cmd: list):
    for i in range(0, 5):
        wait_seconds = 2 ** i
        try:
            status = subprocess.run(cmd)
            if status.returncode != 0:
                print(f'command status was {status}, retrying after {wait_seconds} seconds')
                time.sleep(wait_seconds)
                continue
        except subprocess.CalledProcessError:
            print(f'command failed, retrying after {wait_seconds} seconds')
            time.sleep(wait_seconds)
            continue
        break


def install_dependencies():
    dependencies = [
        {'metaflow_test': 'https://github.com/graviraja/metaflow-test.git'},
    ]
    for dependency in dependencies:
        for k, v in dependency.items():
            try:
                module_ = import_module(k)
            except ModuleNotFoundError:
                system_command_with_retry(['pip', 'install', v])