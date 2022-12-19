import sqlite3 as sql

def base_check_valid(db_name, token, login):
    with sql.connect(db_name) as connect:
        curr = connect.cursor()
        curr.execute(f'SELECT token FROM user WHERE login = "{login}";')
        from_db = curr.fetchone()
        if(from_db[0] = token)
            return True
        return False

def base_update(db_name, token, login):
    with sql.connect(db_name) as connect:
        curr = connect.cursor()
        curr.execute(f"""SELECT login, token FROM user 
                         WHERE login = "{login}";""")
        from_db = curr.fetchone()
        if(len(from_db)):
            curr.execute(f"""DELETE FROM user WHERE login = "{login}";""")
        curr.execute(f"""INSERT INTO user (login, token)
                         VALUES("{login}", "{token}")""")
        connect.commit()
