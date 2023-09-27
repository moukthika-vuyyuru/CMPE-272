# app.py
from flask import Flask, request, jsonify, send_from_directory
import redis
import time
import logging
import gc 

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = Flask(__name__)
r = redis.StrictRedis(host='localhost', port=6379, db=0)

LIMIT = 10  # Requests per hour
WINDOW_SIZE = 20  # 1 hour in seconds

@app.route('/endpoint', methods=['GET'])
def rate_limited_endpoint():

    client_ip = request.remote_addr
    current_time = time.time()

    # Calculate the window's start time
    window_start = float(r.get('window_start') or 0)

    if current_time - window_start > WINDOW_SIZE:
        # If the current time exceeds the window, reset the counter
        r.set('window_start', current_time)
        r.set(client_ip, 1)
    else:
        # Get the current request count
        current_count = int(r.get(client_ip) or 0)

        if current_count < LIMIT:
            # Increment the count for this client
            r.incr(client_ip, 1)
        else:
            # Rate limit exceeded
            return jsonify({"message": "Too many requests!"}), 429

    return jsonify({"message": "Request processed!"}), 200

@app.route('/gc-stats', methods=['GET'])
def gc_stats():
    gc.collect()  # Optionally, trigger a garbage collection before retrieving stats
    return jsonify(gc.get_stats())

if __name__ == '__main__':
    logger.info(f"Start time: {time.time()} seconds")
    #start_time = time.time()
    app.run(host='0.0.0.0', port=5500)
    end_time = time.time()
    l#ogger.info(f"Startup time: {end_time - start_time} seconds")