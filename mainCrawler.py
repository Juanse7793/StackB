# Import necessary libraries
import sqlite3
from datetime import datetime

# Set up SQLite database
def setup_database():
    """Create an SQLite database to store usage data if it does not exist."""
    conn = sqlite3.connect('usage_data.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS usage (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp TEXT,
            filter_type TEXT
        )
    ''')
    conn.commit()
    conn.close()

# Log usage data to the database and text file
def log_request(filter_type):
    """Log the request in the database and a text file."""
    conn = sqlite3.connect('usage_data.db')
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO usage (timestamp, filter_type) 
        VALUES (?, ?)
    ''', (datetime.now().isoformat(), filter_type))
    conn.commit()
    conn.close()
    
    with open('usage_log.txt', 'a') as log_file:
        log_file.write(f"{datetime.now().isoformat()} - Filter: {filter_type}\n")
    
    print(f"Logged request: {datetime.now().isoformat()} - Filter: {filter_type}")
