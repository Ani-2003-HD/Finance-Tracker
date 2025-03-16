# Use Python base image
FROM python:3.11-slim

# Set the working directory
WORKDIR /app

# Copy project files
COPY . /app

# Install dependencies
RUN pip install -r requirements.txt

# Expose the Flask app's default port
EXPOSE 5001

# Run the Flask app
CMD ["python", "app.py"]
