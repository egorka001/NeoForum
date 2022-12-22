from datetime import datetime
from config import get_path
from db_scripts import *
from datetime import datetime

def check_auth(login, token):
    return 1

def my_time():
    return str(datetime.now())

def check_themes(theme):
    if theme in get_themes(get_path()):
        return 1
    return 0

def add_new_theme(theme):
    post_theme(get_path(), theme)

def get_themes_list():
    return get_themes(get_path())

def get_threads_by_theme(theme):
    from_db = select_threads_by_theme(get_path(), theme)
    active = []
    passive = []
    curr_dct = {}
    for i in from_db:
        curr_dct['id'] = i[0]
        curr_dct['login'] = i[1]
        curr_dct['post_count'] = i[2]
        curr_dct['time'] = i[3]
        curr_dct['post_body'] = i[5]
        if(i[4]):
            active.append(curr_dct)
        else:
            passive.append(curr_dct)
        curr_dct = {}

    active = sorted(active, key=lambda x: 
                    datetime.strptime(x['time'], '%Y-%m-%d %H:%M:%S.%f'), 
                    reverse=True)
    passive = sorted(passive, key=lambda x: 
                    datetime.strptime(x['time'], '%Y-%m-%d %H:%M:%S.%f'), 
                    reverse=True)
    out = active + passive 
    return out[:30]

def get_posts_by_thread_id(thread_id):
    from_db = select_posts_by_thread_id(get_path(), thread_id)
    out = []
    curr_dct = {}
    for i in from_db:
        curr_dct['id'] = i[0]
        curr_dct['login'] = i[1]
        curr_dct['post_body'] = i[2]
        curr_dct['post_time'] = i[3]
        out.append(curr_dct)
        curr_dct = {}
    return out

def add_new_post(login, token, thread_id, post_body):
    if(not check_auth(login, token)):
        return 0
    if(thread_id < 0 and get_count['thread_id'] < thread_id):
        return 0
    if(len(post_body) >= 10000):
        return 0
    post_time = my_time()
    post_new_post(get_path(), thread_id, login, post_body, post_time)
    update_thread(get_path(), thread_id, post_time)
    return 1

def add_new_thread(login, token, theme, post_body):
    if(not check_auth(login, token)):
        return 0 
    if(not check_themes(theme)):
        return 0
    if(len(post_body) >= 10000):
        return 0
    post_time = my_time()
    post_new_thread(get_path(), login, theme, post_body, post_time)
