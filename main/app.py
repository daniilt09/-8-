import json
from flask import Flask, render_template
from datetime import datetime
import os
import shutil
import webbrowser

download = True  # менять на False, если не хотим загружать данные с табличек

app = Flask(__name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_PATH = os.path.join(BASE_DIR, 'data', 'data.json')


def create_backup():
    backup_dir = os.path.join(BASE_DIR, 'backups')
    if not os.path.exists(backup_dir):
        os.makedirs(backup_dir)
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    backup_name = os.path.join(backup_dir, f"data_backup_{timestamp}.json")
    shutil.copy2(DATA_PATH, backup_name)


create_backup()


def load():
    with open("data/data.json", "r", encoding="utf-8") as a:
        data = json.load(a)
    return data


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/dict')
def dictionary():
    words = load()
    return render_template('dict.html', words=words)


@app.route('/word/<int:word_id>')
def word_detail(word_id):
    words = load()
    if word_id < len(words):
        word = words[word_id]
        return render_template('word.html', word=word)
    return "Слово не найдено", 404


if __name__ == '__main__':
    webbrowser.open("http://127.0.0.1:5000/")
    app.run(debug=True)
