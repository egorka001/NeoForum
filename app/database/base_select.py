import sqlite3 as sql


def get_threads(db_name):
    with sql.connect(db_name) as connect:
        curr = connect.cursor()
        curr.execute('SELECT thread_id, first_post_id FROM threads;')
        threads_tbl = curr.fetchall()
        info = {}
        for (t_id, p_id) in threads_tbl:
            curr.execute(f"""SELECT post_text FROM posts 
                                    WHERE post_id = {p_id};""")
            text = curr.fetchone()
            info[t_id] = text[0]
    return info


def get_posts(db_name, thread_id):
    info = {}
    with sql.connect(db_name) as connect:
        curr = connect.cursor()
        curr.execute(f"""SELECT post_id, post_text FROM posts 
                            WHERE thread_id = {thread_id};""")
        posts_tbl = curr.fetchall()
        for (p_id, p_text) in posts_tbl:
            info[p_id] = p_text
    return info


def get_count_info(db_name):
    with sql.connect(db_name) as connect:
        curr = connect.cursor()
        curr.execute(f"""SELECT curr_thread, curr_post FROM count
                                WHERE id = 0;""")
        count = curr.fetchone()
        thread_id, post_id = count[0], count[1]
    info = {'thread_id' : thread_id, 'post_id' : post_id}
    return info 
