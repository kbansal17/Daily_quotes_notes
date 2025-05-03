import random
from flask import Flask, render_template, request, redirect
import json
import os
from datetime import datetime

app = Flask(__name__)
NOTES_FILE = 'notes.json'

quotes = [
    "Believe you can and you're halfway there.",
    "Don’t watch the clock; do what it does. Keep going.",
    "Every moment is a fresh beginning.",
    "Stay hungry. Stay foolish.",
    "What we think, we become.",
    "The best way to get started is to quit talking and begin doing.",
    "Act as if what you do makes a difference. It does.",
    "You are never too old to set another goal or to dream a new dream."
]

def load_notes():
    if not os.path.exists(NOTES_FILE):
        return []
    with open(NOTES_FILE, 'r') as f:
        return json.load(f)

@app.route('/')
def index():
    quote = random.choice(quotes)
    return render_template('index.html', quote=quote)

@app.route('/save', methods=['POST'])
def save():
    note_text = request.form.get('note')
    if not note_text:
        return redirect('/')
    notes = load_notes()
    notes.append({
        'text': note_text,
        'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    })
    save_notes(notes)
    return redirect('/notes')

@app.route('/notes')
def view_notes():
    notes = load_notes()
    return render_template('notes.html', notes=notes)

@app.route('/delete/<int:index>', methods=['POST'])
def delete_note(index):
    notes = load_notes()
    if 0 <= index < len(notes):
        notes.pop(index)
        save_notes(notes)
    return redirect('/notes')

@app.route('/edit/<int:index>', methods=['GET', 'POST'])
def edit_note(index):
    notes = load_notes()
    if request.method == 'POST':
        new_text = request.form.get('note')
        if new_text:
            notes[index]['text'] = new_text
            notes[index]['timestamp'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            save_notes(notes)
        return redirect('/notes')
    return render_template('edit.html', index=index, note=notes[index])

def save_notes(notes):
    with open(NOTES_FILE, 'w') as f:
        json.dump(notes, f)
if __name__ == '__main__':
    app.run(debug=True)