FROM python:3.7-slim-buster

WORKDIR /home/app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .
EXPOSE 8080
ENTRYPOINT ["python3", "app.py"]