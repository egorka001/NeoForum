import sys
sys.path.append('../database/')
import base_insert


def insert_new_thread(db_name, post_text):
    if not isinstance(post_text, str):
        print('in insert_new_thread: wrong post_text type')
        return -1
    try:
        out = base_insert.insert_new_thread(db_name, post_text)
    except:
        print('insert_new_thread error')
        return -1
    return out


def insert_new_post(db_name, thread_id, post_text):
    if not isinstance(post_text, str):
        print('in insert_new_post: wrong post_text type')
        return -1
    if not isinstance(thread_id, int):
        print('in insert_new_post: wrong thread_id type')
        return -1 
    if thread_id <= 0:
        print('in insert_new_post: thread_id <= 0')
        return -1 
    try:
        out = base_insert.insert_new_post(db_name, thread_id, post_text)
    except:
        print('insert_new_post error')
        return -1
    return out
