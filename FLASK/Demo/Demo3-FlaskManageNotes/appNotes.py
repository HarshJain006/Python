from flask import Flask, render_template, request, redirect, url_for

appNotes = Flask(__name__)
print("Name of running flask application is : ", appNotes)
# In-memory storage for notes
notes = []

@appNotes.route('/')
def index():
    return render_template('index.html', notes=notes)

@appNotes.route('/add_note', methods=['GET', 'POST'])
def add_note():
    if request.method == 'POST':
        note = request.form['note']
        notes.append(note)
        return redirect(url_for('index'))
    return render_template('add_note.html')

@appNotes.route('/delete_note/<int:note_id>', methods=['GET'])
def delete_note(note_id):
    if 0 <= note_id < len(notes):
        notes.pop(note_id)
    return redirect(url_for('index'))

if __name__ == '__main__':
    appNotes.run(debug=True)