# Base Image
FROM python:3.10-slim

# Set Working Directory
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . .

# Expose port
EXPOSE 5000

# Command to run Flask
CMD ["flask", "run", "--host=0.0.0.0"]
