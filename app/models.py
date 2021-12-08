from . import db
from datetime import datetime

class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50))
    type = db.Column(db.String(20))
    body = db.Column(db.String(220))

#add category id - 1-urgent, 2-not urgent - return as integer.  return all notes to front-end(this is currently being done) then filter by query on the front
