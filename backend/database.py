import sqlite3
import os
from datetime import datetime

DB_PATH = os.path.join(os.path.dirname(__file__), '..', 'database', 'history.db')

def init_db():
    os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS analysis_history (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            filename TEXT,
            content_type TEXT,
            score REAL,
            result_message TEXT,
            timestamp DATETIME
        )
    ''')
    conn.commit()
    conn.close()

def save_analysis(filename, content_type, score, result_message):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO analysis_history (filename, content_type, score, result_message, timestamp)
        VALUES (?, ?, ?, ?, ?)
    ''', (filename, content_type, score, result_message, datetime.now()))
    conn.commit()
    conn.close()

def get_history():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM analysis_history ORDER BY timestamp DESC LIMIT 10')
    rows = cursor.fetchall()
    conn.close()
    return rows

if __name__ == "__main__":
    init_db()
    print("Database initialized.")
