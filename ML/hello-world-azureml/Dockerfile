# Use Python 3.12.3 as base image
FROM python:3.12.3-slim

# Set working directory
WORKDIR /app

# Copy project files
COPY pyproject.toml .
COPY local_inference_server.py .
COPY app/ ./app/
COPY model/ ./model/

# Install production dependencies
RUN pip install --no-cache-dir \
    'azureml-contrib-services>=1.59.0' \
    'azureml-inference-server-http>=1.4.0' \
    'scikit-learn>=1.3.0' \
    'joblib>=1.3.0' \
    'numpy>=1.24.0' \
    'flask>=3.1.2'

# Set model directory environment variable
ENV AZUREML_MODEL_DIR=/app/model

# Expose the port
EXPOSE 5001

# Run the inference server
CMD ["python", "local_inference_server.py"]
