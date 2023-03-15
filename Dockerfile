# Use the official Python 3.9 image as the base image
FROM python:3.9-slim-buster

# Set the working directory to /app
WORKDIR /app
# Copy the requirements file to the container
COPY requirements.txt .

# Install the required packages using pip
RUN pip3 install -r requirements.txt

# Copy the rest of the application files to the container
COPY . .

# Expose port 5000 so that it can be accessed from outside the container
EXPOSE 5000

# Start the Flask application
CMD ["python3", "app.py"]
