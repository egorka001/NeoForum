import sys
sys.path.append('../database/')
import base_insert


def insert_new_thread(db_name, post_text, theme):
    base_insert.insert_new_thread(db_name, post_text, theme)


def insert_new_post(db_name, thread_id, post_text):
    out = base_insert.insert_new_post(db_name, thread_id, post_text)
