# Use a suitable Python base image
FROM python:3.9-slim

# Set a working directory
WORKDIR /app

# Copy requirements.txt and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY main.py .
COPY src ./src

# Set the command to run the application
CMD [ "python", "-m", "main"]
