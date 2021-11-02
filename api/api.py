import time
from datetime import datetime
from flask import Flask

app = Flask(__name__)

@app.route('/time')
def get_current_time():
    ts = time.time()
    return{'time':datetime.fromtimestamp(ts)}