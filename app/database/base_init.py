import sqlite3 as sql

tbl_threads = """
    CREATE TABLE IF NOT EXISTS threads
    (
        thread_id INTEGER PRIMARY KEY,
        first_post_id INTEGER
    );
"""

tbl_posts = """
    CREATE TABLE IF NOT EXISTS posts
    (
        post_id INTEGER PRIMARY KEY,
        post_text TEXT,
        thread_id INTEGER
    );
"""

tbl_count = """
    CREATE TABLE IF NOT EXISTS count
    (
        id INTEGER PRIMARY KEY,
        curr_thread INTEGER,
        curr_post INTEGER
    );
"""

count_init = 'INSERT INTO count (id,curr_thread,curr_post) VALUES (0,0,0);'


def base_init(db_name):
    with sql.connect(db_name) as connect:
        curr = connect.cursor()
        curr.execute(tbl_threads)
        curr.execute(tbl_posts)
        curr.execute(tbl_count)
        try:
            curr.execute(count_init)
        except sql.IntegrityError:
            pass
        connect.commit()
    return 1
