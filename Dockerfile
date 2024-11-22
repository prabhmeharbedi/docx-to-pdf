FROM python:3.9

WORKDIR /app

# Copy all files to the working directory
COPY . .

# Install dependencies
RUN pip install -r requirements.txt

# Expose the port used by the app
EXPOSE 5000

# Start the app with Gunicorn for production
CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:5000", "main:app"]
