import sys
sys.path.append('./database/')
sys.path.append('./interface/')
from init_interface import *
from get_interface import *
from insert_interface import *

def new_thread(db_name):
    text = input('Input first post text: ')
    out = insert_new_thread(db_name, text)
    if out == -1:
        print('error')

def show_threads(db_name):
    out = get_threads(db_name)
    for i in out.keys():
        print(f"{i} : {out[i]}")
    thread = input('Thread number > ')
    return thread

def in_thread(db_name, thread_id):
    status = 'w'
    out = get_posts(db_name, thread_id)
    if out == {}:
        print('error')
        return
    for i in out.keys():
        print(f"{i} : {out[i]}")
    while True:
        status = input('1)Add post\n2)Quit\n> ')
        if status == '1':
            msg = input('Write post > ') 
            insert_new_post(db_name, thread_id, msg)
            out = get_posts(db_name, thread_id)
            for i in out.keys():
                print(f"{i} : {out[i]}")
        elif status == '2':
            return
        else:
            print('Wrong input!\n', end = "")
        
 
with open('./config.txt', 'r') as file:
    db_name = file.readline()
    if db_name[-1] == '\n':
        db_name = db_name[:-1]

db_init(db_name)

status = 'w'
while True:
    status = input('1)Create new thread\n2)Choose thread\n3)Quit\n> ')
    if status == '1':
        new_thread(db_name)
    elif status == '2':
        thread = show_threads(db_name)
        in_thread(db_name, int(thread))
    elif status == '3':
        break
    else:
        print('Wrong input!\n', end = "")
