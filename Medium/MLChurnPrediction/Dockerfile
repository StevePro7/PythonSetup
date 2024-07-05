# Use a Python-based image
FROM python:3.9-slim

COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

WORKDIR /app

COPY . .

CMD ["Python", "src/predict.py"