import requests
import time

# URL of the rate-limited endpoint
URL = "http://localhost:2006/endpoint"

while True:
    try:
        response = requests.get(URL)
        if response.status_code == 200:
            print("Request was successful!")
        else:
            print(f"Received status code: {response.status_code}, message: {response.text}")
    except requests.ConnectionError:
        print("Failed to connect to the server. Make sure the server is running!")
    time.sleep(1)  # Wait for 1 second before the next request
