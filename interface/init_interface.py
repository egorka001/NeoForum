import sys
sys.path.append('../database/')
import base_init


def db_init(db_name):
    out = base_init.base_init(db_name)

if __name__ == "__main__":
    db_init('base.db')
