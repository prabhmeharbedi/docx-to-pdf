# Use the official Python slim image
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy project files to the container
COPY . .

# Install dependencies
RUN pip install -r requirements.txt

# Expose the Flask app port
EXPOSE 5000

# Start the Flask app
CMD ["python", "main.py"]