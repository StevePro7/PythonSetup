# 8. SQL with Python (SQLite)
import sqlite3

# Connect to DB
conn = sqlite3.connect("database.db")
cursor = conn.cursor()

# Execute Queries
cursor.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER, name TEXT)")
cursor.execute("INSERT INTO users VALUES (1, 'Alice')")

# Fetch Data
cursor.execute("SELECT * FROM users")
rows = cursor.fetchall()

conn.commit()
conn.close()