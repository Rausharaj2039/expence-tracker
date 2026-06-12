import sqlite3
from werkzeug.security import generate_password_hash
import os

def get_db():
    """Returns a SQLite connection with row_factory and foreign keys enabled"""
    # Connect to the database file in the project root
    db_path = os.path.join(os.path.dirname(__file__), '..', 'spendly.db')
    print(f"Connecting to: {db_path}")
    conn = sqlite3.connect(db_path)
    # Enable foreign key constraints
    conn.execute('PRAGMA foreign_keys = ON')
    # Return rows as dictionary-like objects
    conn.row_factory = sqlite3.Row
    return conn

def test_count():
    conn = get_db()
    try:
        cursor = conn.execute('SELECT COUNT(*) FROM users')
        count = cursor.fetchone()[0]
        print(f"Count of users: {count}")
        return count
    finally:
        conn.close()

if __name__ == "__main__":
    count = test_count()
    print(f"Final count: {count}")
