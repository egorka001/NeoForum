import sys
sys.path.append('../database/')
import base_select


def get_themes():
    db_name = 'base.db'
    out = base_select.get_themes(db_name)
    return out


def get_threads(theme):
    db_name = 'base.db'
    try:
        out = base_select.get_threads(db_name, theme)
    except:
        print('get_threads error')
        return {} 
    return out


def get_posts(thread_id):
    db_name = 'base.db'
    if not isinstance(thread_id, int):
        print('in get_posts: wrong thread_id type')
        return {} 
    if thread_id <= 0:
        print('in get_posts: thread_id <= 0')
        return {}
    try:
        out = base_select.get_posts(db_name, thread_id)
    except:
        print('get_posts error')
        return {}
    return out


def get_count_info():
    db_name = 'base.db'
    try:
        out = base_select.get_count_info(db_name)
    except:
        print('get_count_info error')
        return {}
    return out
