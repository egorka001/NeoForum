import sqlite3 as sql

global_id_tbl = """   
    CREATE TABLE IF NOT EXISTS global_id 
    (
        id INTEGER PRIMARY KEY,
        post INTEGER,
        thread INTEGER
    );"""

global_id_init = "INSERT INTO global_id (id,post,thread) VALUES (0,0,0);"

themes_tbl = """
    CREATE TABLE IF NOT EXISTS themes 
    (
        id INTEGER PRIMARY KEY,
        theme_name TEXT
    );"""

threads_tbl = """
    CREATE TABLE IF NOT EXISTS threads
    (
        id INTEGER PIRMARY KEY,
        theme_id INTEGER,
        first_post_id INTEGER,
        creator_id INTEGER,
        post_count INTEGER,
        last_update DATETIME,
        status INTEGER
    );"""

posts_tbl = """
    CREATE TABLE IF NOT EXISTS posts
    (
        id INTEGER PIRMARY KEY,
        thread_id INTEGER,
        user_id INTEGER,
        post_body TEXT
        post_pic BLOB,
        post_time DATETIME
    );"""

#users_tbl = """ """

def base_init(db_name):
    with sql.connect(db_name) as conn:
        curr = conn.cursor()
        curr.execute(global_id_tbl)
        curr.execute(themes_tbl)
        curr.execute(threads_tbl)
        curr.execute(posts_tbl)
        try:
            curr.execute(global_id_init)
        except:
            pass
        conn.commit()
    return 1

if __name__ == "__main__":
    base_init("test.db")
