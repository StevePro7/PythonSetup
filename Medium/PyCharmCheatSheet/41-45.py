# 41.
import sqlite3
# Connect to SQLite database
conn = sqlite3.connect('mydatabase.db')
cursor = conn.cursor()
# Execute SQL query
cursor.execute('SELECT * FROM mytable')


# 42.
import zipfile
with zipfile.ZipFile('archive.zip', 'w') as myzip:
    myzip.write('file.txt')
with zipfile.ZipFile('archive.zip', 'r') as myzip:
    myzip.extractall('extracted')


# 43.
import requests
from bs4 import BeautifulSoup
url = 'https://example.com'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
# Extract data from HTML
title = soup.title.text


# 44.
import smtplib
from email.mime.text import MIMEText
# Set up email server
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
# Log in to email account
server.login('your_email@gmail.com', 'your_password')
# Send email
msg = MIMEText('Hello, Python!')
msg['Subject'] = 'Python Email'
server.sendmail('your_email@gmail.com', 'recipient@example.com', msg.as_string())


# 45.
import json
data = {'name': 'John', 'age': 30}
# Write to JSON file
with open('data.json', 'w') as json_file:
    json.dump(data, json_file)
# Read from JSON file
with open('data.json', 'r') as json_file:
    loaded_data = json.load(json_file)
