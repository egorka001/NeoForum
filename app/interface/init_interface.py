import sys
sys.path.append('../database/')
import base_init
from config_read import *


def db_init():
    db_name = config_read()
    try:
        out = base_init.base_init(db_name)
    except:
        print('base_init error')
        return -1
    return out
