from flask import Flask, request, jsonify 
from flask_cors import cross_origin, CORS
import json
import requests
import tokens

import sys
sys.path.append('./data')
from db_scripts import *
from interface import *

app = Flask(__name__)
CORS(app)

@app.route('/api/themes/', methods=['GET'])
@cross_origin()
def send_themes_api():
    """send all themes from forum"""
    if request.method == 'GET':
        out = get_themes_list()
        out = {"themes": out}
        return jsonify(out)

@app.route('/api/themes/<theme_name>', methods=['GET'])
@cross_origin()
def send_threads_api(theme_name):
    """send threads dct from forum"""
    if request.method == 'GET':
        out = get_threads_by_theme(theme_name)
        out = {"threads": out, "theme": theme_name}
        return jsonify(out)

@app.route('/api/thread/<t_id>', methods=['GET'])
@cross_origin()
def send_thread_api(t_id):
    """send current thread"""
    if request.method == 'GET':
        out = get_posts_by_thread_id(t_id)
        out = {"posts": out, "thread_id": t_id}
        return jsonify(out) 

@app.route('/api/new_thread', methods=['POST'])
@cross_origin()
def add_new_thread_hand():
    data = request.json
    login = data["login"]
    token = data["token"]
    theme = data["theme"]
    post_body = data["post_body"]
    if(add_new_thread(login, token, theme, post_body)):
        return "OK" 
    return "DONT OK"

@app.route('/api/new_post', methods=['POST'])
@cross_origin()
def add_new_post_hand():
    data = request.json
    login = data["login"]
    token = data["token"]
    thread_id = int(data["thread_id"])
    post_body = data["post_body"]
    if(add_new_post(login, token, thread_id, post_body)):
        return "OK" 
    return "DONT OK"

@app.route('/api/auth', methods=['POST'])
@cross_origin()
def mega_auth():
    data = request.json
    code = data['code']
    if(code != None):
        response = requests.post(
                    'https://github.com/login/oauth/access_token',
                    data = {'code': code, 
                            'client_id': token.get_client_id(), 
                            'client_secret': token.get_client_secret})
        out = response.text
        token = out[out.find('=') + 1:out.find('&')]
        response = requests.get('https://api.github.com/user',
                            headers={"Authorization" : "Bearer " + token})
        login = json.loads(response.text)
        try:
            only_login = login['login']
        except:
            return "DONT OK" 
        update_base(only_login, token)
        return jsonify({'token': token, 'login': only_login})
    return "DONT OK"

if __name__ == '__main__':
    app.run()

