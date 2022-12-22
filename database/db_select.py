import sqlite3 as sql

def get_global_id(db_name):
    """return current id of last thread and post"""
    with sql.connect(db_name) as conn:
        curr = conn.cursor()
        curr.execute("SELECT thread, post FROM global_id WHERE id = 0;")
        count = curr.fetchone()
        thread_id, post_id = count[0], count[1]
    info = {'thread_id' : thread_id, 'post_id' : post_id}
    return info 

def get_themes(db_name):
    """returns dict of theme names"""
    with sql.connect(db_name) as conn:
        curr = conn.cursor()
        curr.execute("SELECT theme_name FROM themes")
        names = curr.fetchall()
    out = []
    for i in names:
        out.append(i[0]) 
    out = {"themes" : out}
    return out

def get_theme_threads(db_name, theme_name):
    """return list of threads of one theme, and first first post text"""
    with sql.connect(db_name) as conn:
        curr = conn.cursor()
        curr.execute(f"""SELECT id FROM themes 
                         WHERE theme_name = {theme_name}""")
        theme_id = curr.fetchone()[0]
        curr.execute(f"""SELECT id, post_body FROM threads 
                         JOIN posts ON threads.first_post_id = posts.id
                         WHERE theme_id = {theme_id}""")
        threads = curr.fetchall()
    list_threads = []
    for i in threads:
        list_threads.append({"id": i[0], "thread_body": i[1]})
    out = {"threads" : list_threads}
    return out 

def get_thread(db_name, thread_id):
    """return posts from thread and some additional info"""
    pass

if __name__ == "__main__":
    print(get_global_id("test.db"))
    print(get_themes("test.db"))
