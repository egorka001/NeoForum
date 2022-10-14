from flask import Flask, render_template, request
app = Flask(__name__, template_folder='./app/templates/')

import sys
sys.path.append('./app/database/')
sys.path.append('./app/interface/')
from init_interface import *
from get_interface import *
from insert_interface import *

@app.route('/')
def get_main_page():
    thread_dct = get_threads(db_name)
    return render_template('index.html', threads=thread_dct) 

@app.route('/<thread_id>')
def show_thread(thread_id):
    post_dct = get_posts(db_name, int(thread_id))
    return render_template('thread.html', thread_id=int(thread_id),
                                                    posts=post_dct)

@app.route('/newthread')
def add_new_thread():
    return render_template('newthreadform.html')

@app.route('/addthread', methods=['POST'])
def addthread():
    if request.method == 'POST':
        thread_id = insert_new_thread(db_name, request.form['posttext'])
    if thread_id > 0:
        return render_template('success_thread.html', thread_id=thread_id) 
    else:
        return render_template('fail.html')

@app.route('/newpost<thread_id>')
def add_new_post(thread_id):
    return render_template('newpostform.html', thread_id=int(thread_id))

@app.route('/addpost<thread_id>', methods=['POST'])
def addpost(thread_id):
    if request.method == 'POST':
        thread_id = int(thread_id)
        post_id = insert_new_post(db_name, thread_id,
                                           request.form['posttext'])
    if post_id > 0:
        return render_template('success_post.html', thread_id=thread_id)
    else:
        return render_template('fail.html')

if __name__ == '__main__':
    with open('./config.txt', 'r') as file:
        db_name = file.readline()
        if db_name[-1] == '\n':
            db_name = db_name[:-1]

    db_init(db_name)
    app.run()
