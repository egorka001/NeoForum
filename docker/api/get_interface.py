import sys
sys.path.append('../database/')
import base_select


def get_themes(db_name):
    out = base_select.get_themes(db_name)
    return out


def get_threads(db_name, theme):
    out = base_select.get_threads(db_name, theme)
    return out


def get_posts(db_name, thread_id):
    out = base_select.get_posts(db_name, thread_id)
    return out


def get_count_info(db_name):
    out = base_select.get_count_info(db_name)
    return out
