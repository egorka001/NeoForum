threads_sample = """ {"threads" : [{"id": "1", "creator_name" : "Егор", "thread_title" : "Какой крутой сайт", "thread_body" : "Вообще очень рад, что всё так получается!", "pic" : "base64 pic code"},{"id": "2", "creator_name" : "Ася", "thread_title" : "Реально, очень крутой сайт", "thread_body" : "Вот бы такие почаще делали", "pic" : "base64 pic code"},{"id": "3", "creator_name" : "Лена", "thread_title" : "Продам гараж", "thread_body" : "Очень хороший гараж!", "pic" : "base64 pic code"},{"id": "4", "creator_name" : "Антошка", "thread_title" : "Очень хочу картошки", "thread_body" : "Кто со мной копать картошку", "pic" : "base64 pic code"},{"id": "5", "creator_name" : "Кирилл", "thread_title" : "Помогите с ассемблером", "thread_body" : "Запутался в мнемониках опкодов, очень страшно выходит", "pic" : "base64 pic code"},{"id": "6", "creator_name" : "Паша", "thread_title" : "Скоро этот сайт ляжет", "thread_body" : "И ничего с этим поделать никто не сможет", "pic" : "base64 pic code"}]}"""

themes_sample = """{"themes" : ["sport", "motosport", "programming", "offtop"]}"""

thread_sample = """{"creator_name" : "Максим", "thread_titile":"Лечу в сочи", "posts" : [{"post_id" : "0", "date" : "01.12.2022", "time" : "13:41", "post_creator" : "Максим", "post_text" : "Что лучше с собой взять на отдых?", "post_pic" : "base64 pic code"},{"post_id" : "1", "date" : "01.12.2022", "time" : "13:42", "post_creator" : "Егор", "post_text" : "Средство от загара", "post_pic" : "base64 pic code"},{"post_id" : "2", "date" : "01.12.2022", "time" : "13:43", "post_creator" : "Антон", "post_text" : "Лучше ничего с собой не брать, так на легке поехать", "post_pic" : ""},{"post_id" : "3", "date" : "01.12.2022", "time" : "13:44", "post_creator" : "Лена", "post_text" : "Может у меня всё таки купят гараж?", "post_pic" : "base64 pic code"}]}"""

from flask import Flask, render_template, request, send_from_directory 
from flask import jsonify

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
        return jsonify(themes_sample)

@app.route('/api/themes/sport', methods=['GET'])
@app.route('/api/themes/motosport', methods=['GET'])
@app.route('/api/themes/programming', methods=['GET'])
@app.route('/api/themes/offtop', methods=['GET'])
def send_threads_api():
    """send threads dct from forum"""
    if request.method == 'GET':
        return jsonify(threads_sample)

@app.route('/api/thread/1', methods=['GET'])
@app.route('/api/thread/2', methods=['GET'])
@app.route('/api/thread/3', methods=['GET'])
@app.route('/api/thread/4', methods=['GET'])
@app.route('/api/thread/5', methods=['GET'])
def send_thread_api():
    """send current thread"""
    if request.method == 'GET':
        return jsonify(thread_sample) 

if __name__ == '__main__':
    app.run()





