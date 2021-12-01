from flask import Blueprint, jsonify, request
from . import db
from .models import Note

main = Blueprint('main', __name__)

@main.route('/add_note', methods=['POST'])
def add_note():
    note_data = request.get_json()

    new_note = Note(title=note_data['title'], type=note_data['type'], body=note_data['body'])

    db.session.add(new_note)
    db.session.commit()

    return 'Done!', 201


@main.route('/notes')
def notes():
    #sql alchemy result, must turn into something that can be read by json
    note_list = Note.query.all()
    notes = []

    for note in note_list:
        notes.append({'title' : note.title, 'type' : note.type, 'body' : note.body})

    return jsonify({'notes' : notes})