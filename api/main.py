from flask import Flask, render_template, request, send_from_directory 
from flask import jsonify

import sys
sys.path.append('../database/')
sys.path.append('../interface/')
from init_interface import *
from get_interface import *
from insert_interface import *
from config import *

app = Flask(__name__)

@app.route('/favicon.ico', methods=['GET'])
def favicon():
    if request.method == 'GET':
        return send_from_directory('static', 'favicon.ico') 

@app.route('/', methods=['GET'])
def send_base():
    """send base index.html page"""
    if request.method == 'GET':
        return render_template('index.html')

@app.route('/api/', methods=['GET'])
def send_api():
    """send info page about api, api.html"""
    if request.method == 'GET':
        return render_template('api.html')

@app.route('/api/themes/', methods=['GET'])
def send_themes_api():
    """send all themes from forum"""
    if request.method == 'GET':
        return jsonify(get_themes(get_path()))

@app.route('/api/themes/<theme_name>', methods=['GET'])
def send_threads_api(theme_name):
    """send threads dct from forum"""
    if request.method == 'GET':
        return jsonify(get_threads(get_path(), theme_name))

@app.route('/api/thread/<t_id>', methods=['GET'])
def send_thread_api(t_id):
    """send current thread"""
    if request.method == 'GET':
        return jsonify(get_posts(get_path(),int(t_id))) 

@app.route('/api/new_thread')
def add_new_thread():
    theme = request.args.get('theme')
    post_text = request.args.get('post_text')
    if(theme != None and post_text != None):
        insert_new_thread(get_path(), post_text, theme)
        return "1" 
    return "0"

@app.route('/api/new_post')
def add_new_post():
    t_id = request.args.get('t_id')
    post_text = request.args.get('post_text')
    if(t_id != None and post_text != None):
        insert_new_post(get_path(), int(t_id), post_text)
        return "1" 
    return "0"

if __name__ == '__main__':
    app.run()





