import sqlite3 as sql

def get_count(db_name):
    """get current count status"""
    with sql.connect(db_name) as connect:
        curr = connect.cursor()
        curr.execute(f"""SELECT thread, post FROM global_id 
                                WHERE id = 0;""")
        count = curr.fetchone()
        thread_id, post_id = count[0], count[1]
    info = {'thread_id' : thread_id, 'post_id' : post_id}
    return info 

def update_post_count(db_name):
    """increment and return post count"""
    with sql.connect(db_name) as connect:
        curr = connect.cursor()
        curr.execute('UPDATE global_id SET post = post + 1;')
        connect.commit()
    count = get_count(db_name)
    post_count = count['post_id']
    return post_count

def update_thread_count(db_name):
    """increment and return thread count"""
    with sql.connect(db_name) as connect:
        curr = connect.cursor()
        curr.execute('UPDATE global_id SET thread = thread + 1;')
        connect.commit()
    count = get_count(db_name)
    thread_count = count['thread_id']
    return thread_count

def post_theme(db_name, theme_name):
    """post new theme in themes table"""
    with sql.connect(db_name) as connect:
        curr = connect.cursor()
        curr.execute(f"""INSERT INTO themes (theme_name) 
                         VALUES ("{theme_name}");""")
        connect.commit()

def get_themes(db_name):
    """get list of themes"""
    with sql.connect(db_name) as connect:
        curr = connect.cursor()
        curr.execute('SELECT theme_name FROM themes') 
        themes = curr.fetchall()
    out = []
    for i in themes:
        out.append(i[0])
    return out

def post_new_post(db_name, thread_id, login, post_body, post_time):
    """post new post in posts table"""
    post_id = update_post_count(db_name)
    with sql.connect(db_name) as connect:
        curr = connect.cursor()
        curr.execute(f"""INSERT INTO posts (id, thread_id, login,
                         post_body, post_time) 
                         VALUES ({post_id}, {thread_id}, "{login}", 
                         "{post_body}", "{post_time}");""")
        connect.commit()
    return post_id 

def update_thread(db_name, thread_id, post_time):
    """update post_count + 1, checks status, last update"""
    with sql.connect(db_name) as connect:
        curr = connect.cursor()
        curr.execute(f"""UPDATE threads SET post_count = post_count + 1
                        WHERE id = {thread_id};""")
        curr.execute(f"""UPDATE threads SET last_update = "{post_time}"
                         WHERE id = {thread_id};""")
        curr.execute(f"""SELECT post_count FROM threads
                         WHERE id = {thread_id}""")
        post_count = curr.fetchone()
        if(post_count[0] > 10):
            curr.execute(f"""UPDATE threads SET status = 0
                            WHERE id = {thread_id};""")
        connect.commit()

def post_new_thread(db_name, login, theme, post_body, post_time):
    """post new thread and first post"""
    thread_id = update_thread_count(db_name)
    post_id = update_post_count(db_name)
    with sql.connect(db_name) as connect:
        curr = connect.cursor()
        curr.execute(f"""INSERT INTO threads 
                        (id, theme, first_post_id, login, post_count, 
                        last_update, status) 
                        VALUES ({thread_id}, "{theme}", {post_id},
                        "{login}", 1, "{post_time}", 1);""")
        curr.execute(f"""INSERT INTO posts (id, thread_id, login,
                        post_body, post_time)
                        VALUES ({post_id}, {thread_id}, "{login}",
                        "{post_body}", "{post_time}");""")
        connect.commit()
    return thread_id

def select_posts_by_thread_id(db_name, thread_id):
    with sql.connect(db_name) as connect:
        curr = connect.cursor()
        curr.execute(f"""SELECT id, login, post_body, post_time
                         FROM posts WHERE thread_id = {thread_id}""")
        out = curr.fetchall()
    return out

def select_threads_by_theme(db_name, theme):
    with sql.connect(db_name) as connect:
        curr = connect.cursor()
        curr.execute(f"""SELECT threads.id, threads.login, post_count, 
                         last_update, status, posts.post_body 
                         FROM threads JOIN posts ON
                         threads.first_post_id = posts.id 
                         WHERE theme = "{theme}";""")
        out = curr.fetchall()
    return out

