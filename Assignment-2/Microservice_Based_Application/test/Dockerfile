# Use an official Python runtime as the parent image
FROM python:3.9-slim

# Set the working directory in the container to /app
WORKDIR /app

COPY script.py /app/

# Install requests library
RUN pip install requests

# Start the test script
CMD ["python", "script.py"]
