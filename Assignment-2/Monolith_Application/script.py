import requests
import time

# URL of the rate-limited endpoint
URL = "http://127.0.0.1:51790/endpoint"  # Use the service name defined in your Kubernetes YAML

counter =0
# Number of requests to make
num_requests = 100

for _ in range(num_requests):
    try:
        response = requests.get(URL)
        if response.status_code == 200:
            counter+=1
            print(f"Request {counter} was successful!")
        else:
            print(f"Received status code: {response.status_code}, message: {response.text}")
    except requests.ConnectionError:
        print("Failed to connect to the server. Make sure the server is running!")
    time.sleep(1)  # Wait for 1 second before the next request
