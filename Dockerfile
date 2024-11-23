FROM ubuntu:20.04

# Prevent tzdata from prompting for timezone
ENV DEBIAN_FRONTEND=noninteractive

# Install system dependencies
RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    libreoffice \
    unoconv \
    qpdf \
    tzdata \
    && rm -rf /var/lib/apt/lists/*

# Set the timezone to UTC (or your preferred timezone)
RUN ln -fs /usr/share/zoneinfo/Etc/UTC /etc/localtime && dpkg-reconfigure --frontend noninteractive tzdata

# Set working directory
WORKDIR /app

# Copy project files
COPY . .

# Install Python dependencies
RUN pip3 install -r requirements.txt

# Expose Flask app port
EXPOSE 5000

# Run the Flask app
CMD ["python3", "main.py"]
