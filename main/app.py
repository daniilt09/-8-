import json
from flask import Flask, render_template
from datetime import datetime
import os
import shutil

app = Flask(__name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_PATH = os.path.join(BASE_DIR, 'data', 'data.json')
BACKUP_DIR = os.path.join(BASE_DIR, 'backups')

def create_backup():
    if os.path.exists(DATA_PATH):
        if not os.path.exists(BACKUP_DIR):
            os.makedirs(BACKUP_DIR)
        
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        backup_name = os.path.join(BACKUP_DIR, f"data_backup_{timestamp}.json")
        
        shutil.copy2(DATA_PATH, backup_name)

def load():
    if os.path.exists(DATA_PATH):
        with open(DATA_PATH, "r", encoding="utf-8") as a:
            return json.load(a)
    return []

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
    create_backup()
    app.run(debug=True)
