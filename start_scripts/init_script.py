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
        theme_name TEXT PRIMARY KEY
    );"""

threads_tbl = """
    CREATE TABLE IF NOT EXISTS threads
    (
        id INTEGER PRIMARY KEY,
        theme TEXT,
        first_post_id INTEGER,
        login TEXT,
        post_count INTEGER,
        last_update TEXT,
        status INTEGER
    );"""

posts_tbl = """
    CREATE TABLE IF NOT EXISTS posts
    (
        id INTEGER PRIMARY KEY,
        thread_id INTEGER,
        login TEXT,
        post_body TEXT,
        post_time TEXT 
    );"""

users_tbl = """ 
    CREATE TABLE IF NOT EXISTS users
    (
        login TEXT PRIMARY KEY,
        token TEXT,
        status INTEGER
    );"""

def base_init(db_name):
    with sql.connect(db_name) as conn:
        curr = conn.cursor()
        curr.execute(global_id_tbl)
        curr.execute(themes_tbl)
        curr.execute(threads_tbl)
        curr.execute(posts_tbl)
        curr.execute(users_tbl)
        try:
            curr.execute(global_id_init)
        except:
            pass
        conn.commit()
    return 1

if __name__ == "__main__":
    base_init('base.db')

    theme_list = ['Спорт', 'Музыка', 'Кино', 'Велосипеды',
                  'Мультфильмы', 'Книги', 'It', 'Игры', 'Оффтоп']

    for theme in theme_list:
        with sql.connect('base.db') as conn:
            curr = conn.cursor()
            curr.execute(f"""INSERT INTO themes (theme_name) 
                             VALUES ("{theme}");""")
            conn.commit()


