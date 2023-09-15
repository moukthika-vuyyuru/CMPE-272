# app.py
from flask import Flask, request, jsonify, send_from_directory
import redis
import time
import cProfile
import logging
import pstats
import gc 

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = Flask(__name__)
r = redis.StrictRedis(host='redis-rate-limiter', port=6379, db=0)

LIMIT = 100  # Requests per hour
WINDOW_SIZE = 60  # 1 hour in seconds

# Create a global Stats object
global_stats = pstats.Stats()

@app.route('/endpoint', methods=['GET'])
def rate_limited_endpoint():
    pr = cProfile.Profile()
    pr.enable()

    client_ip = request.remote_addr
    current_time = time.time()

    # Calculate the window's start time
    window_start = current_time - WINDOW_SIZE

    # Get the number of requests made by this client in this window
    requests_made = int(r.get(client_ip) or 0)
    logger.info(f"Client IP: {client_ip}, Current Time: {current_time}, Window Start: {window_start}, Requests Made: {requests_made}")

    if requests_made < LIMIT:
        # Process request and increment the count
        r.incr(client_ip, 1)
        r.expire(client_ip, WINDOW_SIZE)  # Set expiration for the key
        pr.disable()
        global_stats.add(pr)
        return jsonify({"message": "Request processed!"}), 200
    else:
        # Rate limit exceeded
        return jsonify({"message": "Too many requests!"}), 429

@app.route('/get_profile_data', methods=['GET'])
def get_profile_data():
    global_stats.dump_stats("/app/prof_output.pstats")
    return send_from_directory('/app', 'prof_output.pstats')

@app.route('/gc-stats', methods=['GET'])
def gc_stats():
    gc.collect()  # Optionally, trigger a garbage collection before retrieving stats
    return jsonify(gc.get_stats())

if __name__ == '__main__':
    logger.info(f"Start time: {time.time()} seconds")
    #start_time = time.time()
    app.run(host='0.0.0.0', port=5000)
    end_time = time.time()
    logger.info(f"Startup time: {end_time - start_time} seconds")