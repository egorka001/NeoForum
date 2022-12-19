from flask import Flask, render_template, request, send_from_directory 
from flask import jsonify
from flask_cors import cross_origin, CORS

import sys
import json
import requests
sys.path.append('../database/')
sys.path.append('../interface/')
from init_interface import *
from get_interface import *
from insert_interface import *
from auth_interface import *
from config import *

app = Flask(__name__)
CORS(app)


@app.route('/favicon.ico', methods=['GET'])
@cross_origin()
def favicon():
    if request.method == 'GET':
        return send_from_directory('static', 'favicon.ico') 

@app.route('/', methods=['GET'])
@cross_origin()
def send_base():
    """send base index.html page"""
    if request.method == 'GET':
        return render_template('index.html')

@app.route('/api/', methods=['GET'])
@cross_origin()
def send_api():
    """send info page about api, api.html"""
    if request.method == 'GET':
        return render_template('api.html')

@app.route('/api/themes/', methods=['GET'])
@cross_origin()
def send_themes_api():
    """send all themes from forum"""
    if request.method == 'GET':
        return jsonify(get_themes(get_path()))

@app.route('/api/themes/<theme_name>', methods=['GET'])
@cross_origin()
def send_threads_api(theme_name):
    """send threads dct from forum"""
    if request.method == 'GET':
        return jsonify(get_threads(get_path(), theme_name))

@app.route('/api/thread/<t_id>', methods=['GET'])
@cross_origin()
def send_thread_api(t_id):
    """send current thread"""
    if request.method == 'GET':
        return jsonify(get_posts(get_path(),int(t_id))) 

@app.route('/api/new_thread', methods=['POST'])
@cross_origin()
def add_new_thread():
    data = request.json
    theme = data['theme']
    post_text = data['post_text']
    token = data['token']
    user = data['user']
    if(theme != None or post_text != None):
        if(check_valid(get_path(), token, user)):
            insert_new_thread(get_path(), post_text, theme)
            return "1" 
    return "0"

@app.route('/api/new_post', methods=['POST'])
@cross_origin()
def add_new_post():
    data = request.json
    t_id = data['t_id']
    post_text = data['post_text']
    token = data['token']
    user = data['user']
    if(t_id != None or post_text != None):
        if(check_valid(get_path(), token, user)):
            insert_new_post(get_path(), int(t_id), post_text)
            return "1" 
    return "0"

@app.route('/api/auth', methods=['POST'])
@cross_origin()
def mega_auth():
    data = request.json
    code = data['code']
    if(code != None):
        response = requests.post(
                    'https://github.com/login/oauth/access_token',
                    data = {'code': code, 
                            'client_id': '89fdb6f152e43d0652a8', 
            'client_secret': '2396e06c97d314b0bd5cedf474cef158347d5834'})
        out = response.text
        token = out[out.find('=') + 1:out.find('&')]
        response = requests.get('https://api.github.com/user',
                            headers={"Authorization" : "Bearer " + token})
        login = json.loads(response.text)
        update_base(get_path(), token, login)
        return jsonify({'token': token, 'login': login})
    return "0"

if __name__ == '__main__':
    app.run()

