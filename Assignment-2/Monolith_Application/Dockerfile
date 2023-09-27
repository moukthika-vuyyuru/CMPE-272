# Use an official Python runtime as the parent image
FROM python:3.9-slim

# Set the working directory in the container to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install Flask and other requirements
RUN pip install Flask redis

# Make port 5000 available to the world outside this container
EXPOSE 5500

# Define environment variable
ENV NAME World

# By default, run app.py when the container launches
CMD ["bash", "start.sh"]
