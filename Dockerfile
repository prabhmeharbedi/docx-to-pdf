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

# Set the timezone to UTC
RUN ln -snf /usr/share/zoneinfo/UTC /etc/localtime && echo "UTC" > /etc/timezone

# Log versions for debugging
RUN python3 --version && pip3 --version && libreoffice --version && unoconv --version && qpdf --version

# Set working directory
WORKDIR /app

# Copy project files
COPY . .

# Install Python dependencies
RUN pip3 install -r requirements.txt

# Ensure unoconv is linked properly (fixes some deployment issues)
RUN ln -s /usr/bin/python3 /usr/bin/python && chmod +x /usr/bin/unoconv

# Expose Flask app port
EXPOSE 5000

# Default command to run the application
CMD ["python3", "main.py"]
