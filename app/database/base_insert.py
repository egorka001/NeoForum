import sqlite3 as sql
from base_select import get_count_info


def update_thread_count(db_name):
    with sql.connect(db_name) as connect:
        curr = connect.cursor()
        curr.execute('UPDATE count SET curr_thread = curr_thread + 1;')
        connect.commit()
    count = get_count_info(db_name)
    thread_count = count['thread_id']
    return thread_count


def update_post_count(db_name):
    with sql.connect(db_name) as connect:
        curr = connect.cursor()
        curr.execute('UPDATE count SET curr_post = curr_post + 1;')
        connect.commit()
    count = get_count_info(db_name)
    post_count = count['post_id']
    return post_count


def insert_new_thread(db_name, post_text):
    thread_id = update_thread_count(db_name)
    post_id = update_post_count(db_name)
    with sql.connect(db_name) as connect:
        curr = connect.cursor()
        curr.execute(f"""INSERT INTO threads (thread_id, first_post_id) 
                                    VALUES ({thread_id}, {post_id});""")
        curr.execute(f"""INSERT INTO posts (post_id, post_text, thread_id) 
                        VALUES({post_id}, '{post_text}', {thread_id});""")
        connect.commit()
    return thread_id
    

def insert_new_post(db_name, thread_id, post_text):
    post_id = update_post_count(db_name)
    with sql.connect(db_name) as connect:
        curr = connect.cursor()
        curr.execute(f"""INSERT INTO posts (post_id, post_text, thread_id) 
                        VALUES({post_id}, '{post_text}', {thread_id});""")
        connect.commit()
    return post_id
