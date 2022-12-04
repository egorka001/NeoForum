threads_sample = """ {"threads" : [{"id": "1", "creator_name" : "Егор", "thread_title" : "Какой крутой сайт", "thread_body" : "Вообще очень рад, что всё так получается!", "pic" : "base64 pic code"},{"id": "2", "creator_name" : "Ася", "thread_title" : "Реально, очень крутой сайт", "thread_body" : "Вот бы такие почаще делали", "pic" : "base64 pic code"},{"id": "3", "creator_name" : "Лена", "thread_title" : "Продам гараж", "thread_body" : "Очень хороший гараж!", "pic" : "base64 pic code"},{"id": "4", "creator_name" : "Антошка", "thread_title" : "Очень хочу картошки", "thread_body" : "Кто со мной копать картошку", "pic" : "base64 pic code"},{"id": "5", "creator_name" : "Кирилл", "thread_title" : "Помогите с ассемблером", "thread_body" : "Запутался в мнемониках опкодов, очень страшно выходит", "pic" : "base64 pic code"},{"id": "6", "creator_name" : "Паша", "thread_title" : "Скоро этот сайт ляжет", "thread_body" : "И ничего с этим поделать никто не сможет", "pic" : "base64 pic code"}]}"""

themes_sample = """{"themes" : ["sport", "motosport", "programming", "offtop"]}"""

thread_sample = """{"creator_name" : "Максим", "thread_titile":"Лечу в сочи", "posts" : [{"post_id" : "0", "date" : "01.12.2022", "time" : "13:41", "post_creator" : "Максим", "post_text" : "Что лучше с собой взять на отдых?", "post_pic" : "base64 pic code"},{"post_id" : "1", "date" : "01.12.2022", "time" : "13:42", "post_creator" : "Егор", "post_text" : "Средство от загара", "post_pic" : "base64 pic code"},{"post_id" : "2", "date" : "01.12.2022", "time" : "13:43", "post_creator" : "Антон", "post_text" : "Лучше ничего с собой не брать, так на легке поехать", "post_pic" : ""},{"post_id" : "3", "date" : "01.12.2022", "time" : "13:44", "post_creator" : "Лена", "post_text" : "Может у меня всё таки купят гараж?", "post_pic" : "base64 pic code"}]}"""

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def send_base():
    """send base index.html page"""
    return render_template('index.html')

@app.route('/api/')
def send_api():
    """send info page about api, api.html"""
    return render_template('api.html')

@app.route('/api/themes/')
def send_themes_api():
    """send all themes from forum"""
    return themes_sample 

@app.route('/api/threads_sport')
@app.route('/api/threads_motosport')
@app.route('/api/threads_programming')
@app.route('/api/threads_offtop')
def send_threads_api():
    """send threads dct from forum"""
    return threads_sample

@app.route('/api/thread_1')
@app.route('/api/thread_2')
@app.route('/api/thread_3')
@app.route('/api/thread_4')
@app.route('/api/thread_5')
def send_thread_api():
    """send current thread"""
    return thread_sample 

if __name__ == '__main__':
    app.run()





