FROM --platform=linux/amd64 python:3.9


WORKDIR /app

# Copy all files to the working directory
COPY . .

# Install dependencies
RUN pip install -r requirements.txt

# Expose the port used by the app
EXPOSE 5000

# Start the app with Gunicorn for production
CMD ["python", "main.py"]
