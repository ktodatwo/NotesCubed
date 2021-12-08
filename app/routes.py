from app import app
from datetime import datetime
import time


#route to fetch timestamp
@app.route('/time')
def get_current_time():
    ts = time.time()
    return{'time': datetime.fromtimestamp(ts)}