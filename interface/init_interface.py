import sys
sys.path.append('../database/')
import base_init


def db_init():
    db_name = 'base.db'
    try:
        out = base_init.base_init(db_name)
    except:
        print('base_init error')
        return -1

if __name__ == "__main__":
    db_init()
