#!/bin/bash

echo "Building the Docker image..."
docker build -t docx-to-pdf .

echo "Running the Docker container..."
docker run -d -p 8080:5000 docx-to-pdf

echo "Your app is now running at http://127.0.0.1:8080"
