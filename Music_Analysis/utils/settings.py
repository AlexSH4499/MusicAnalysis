import os, fnmatch
import sys
import inspect
import platform
import threading

from platform import system

from pathlib import Path



ROOT_DIR = None

current_platform =None

try:
    current_platform = system()

    if current_platform.lower() =='windows':
        pass

    if current_platform.lower() =="linux"
        pass
    else:
        raise ValueError(f"Sorry your platform [{current_platform}] is not currently supported!\n")

except Exception as e:
    print(e)
    sys.exit(-1)
    pass

def get_project_root()->Path:
    return Path(__file__).parent.parent

def find(name, path):
    for root, dirs,files in os.walk(path):
        if name in files:
            yield os.path.join(root , name)

def find_pattern(pattern,path):
    '''works like *.txt with grep on linux systems'''
    for root, dirs, files in os.walk(path):
        for name in files:
            if fnmatch.fnmatch(name, pattern):
                yield os.path.join(root, name)

def setup():
    main_id = None
    for t in threading.enumerate():
        if t.name == 'MainThread':
            main_id = t.ident
            break

    if not main_id:
        raise RuntimeError("Main thread exited before execution")

    current_main_frame = sys._current_frames()[main_id]
    base_frame = inspect.getouterframes(current_main_frame)[-1]

    if system().lower() == 'windows':
        filename = base_frame.filename
    else:
        filename = base_frame[0].f_code.co_filename

    global ROOT_DIR
    ROOT_DIR = os.path.dirname(os.path.abspath(filename))
    return ROOT_DIR