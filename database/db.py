import sqlite3
from werkzeug.security import generate_password_hash
import os

def get_db():
    """Returns a SQLite connection with row_factory and foreign keys enabled"""
    # Connect to the database file in the project root
    db_path = os.path.join(os.path.dirname(__file__), '..', 'spendly.db')
    conn = sqlite3.connect(db_path)
    # Enable foreign key constraints
    conn.execute('PRAGMA foreign_keys = ON')
    # Return rows as dictionary-like objects
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    """Creates all tables using CREATE TABLE IF NOT EXISTS"""
    conn = get_db()
    try:
        # Create users table
        conn.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                email TEXT UNIQUE NOT NULL,
                password_hash TEXT NOT NULL,
                created_at TEXT DEFAULT (datetime('now'))
            )
        ''')

        # Create expenses table
        conn.execute('''
            CREATE TABLE IF NOT EXISTS expenses (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER NOT NULL,
                amount REAL NOT NULL,
                category TEXT NOT NULL,
                date TEXT NOT NULL,
                description TEXT,
                created_at TEXT DEFAULT (datetime('now')),
                FOREIGN KEY (user_id) REFERENCES users (id)
            )
        ''')

        conn.commit()
    finally:
        conn.close()

def seed_db():
    """Inserts sample data for development"""
    conn = get_db()
    try:
        # Check if we already have users
        cursor = conn.execute('SELECT COUNT(*) FROM users')
        count = cursor.fetchone()[0]

        if count > 0:
            # Already seeded, return early
            return

        # Insert demo user
        password_hash = generate_password_hash('demo123')
        conn.execute('''
            INSERT INTO users (name, email, password_hash)
            VALUES (?, ?, ?)
        ''', ('Demo User', 'demo@spendly.com', password_hash))

        # Get the user ID
        user_id = conn.execute('SELECT last_insert_rowid()').fetchone()[0]

        # Sample expenses data
        sample_expenses = [
            # Food
            (user_id, 15.50, 'Food', '2026-06-01', 'Lunch at cafe'),

            # Transport
            (user_id, 8.00, 'Transport', '2026-06-02', 'Bus fare'),

            # Bills
            (user_id, 120.00, 'Bills', '2026-06-01', 'Electricity bill'),

            # Health
            (user_id, 35.00, 'Health', '2026-06-10', 'Pharmacy'),

            # Entertainment
            (user_id, 25.00, 'Entertainment', '2026-06-12', 'Movie tickets'),

            # Shopping
            (user_id, 42.75, 'Shopping', '2026-06-05', 'New clothes'),

            # Other
            (user_id, 18.00, 'Other', '2026-06-08', 'Gift for friend'),

            # Additional Food expense to make 8 total
            (user_id, 30.25, 'Food', '2026-06-10', 'Dinner at restaurant'),
        ]

        # Insert sample expenses
        conn.executemany('''
            INSERT INTO expenses (user_id, amount, category, date, description)
            VALUES (?, ?, ?, ?, ?)
        ''', sample_expenses)

        conn.commit()
    finally:
        conn.close()