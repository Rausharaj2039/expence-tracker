import sqlite3
import os
import random
from werkzeug.security import generate_password_hash

def get_db():
    """Returns a SQLite connection with row_factory and foreign keys enabled"""
    # Connect to the database file in the project root
    db_path = os.path.join(os.path.dirname(__file__), 'spendly.db')
    conn = sqlite3.connect(db_path)
    # Enable foreign key constraints
    conn.execute('PRAGMA foreign_keys = ON')
    # Return rows as dictionary-like objects
    conn.row_factory = sqlite3.Row
    return conn

def generate_indian_name():
    # Common Indian first names (across regions)
    first_names = [
        'Aarav', 'Vivaan', 'Aditya', 'Vihaan', 'Arjun', 'Sai', 'Reyansh', 'Krishna',
        'Ishaan', 'Shaurya', 'Atharv', 'Naithik', 'Vivaan', 'Arnav', 'Kiaan',
        'Aisha', 'Ananya', 'Diya', 'Pari', 'Anvi', 'Myra', 'Kiara', 'Saanvi',
        'Advika', 'Inaya', 'Navya', 'Priya', 'Deepika', 'Neha', 'Pooja', 'Sonam'
    ]
    # Common Indian last names
    last_names = [
        'Sharma', 'Verma', 'Patel', 'Singh', 'Kumar', 'Joshi', 'Desai', 'Reddy',
        'Nair', 'Iyer', 'Agarwal', 'Gupta', 'Malhotra', 'Chopra', 'Mehta',
        'Kapoor', 'Khanna', 'Malik', 'Kaur', 'Das', 'Banerjee', 'Chatterjee'
    ]
    first = random.choice(first_names)
    last = random.choice(last_names)
    return first, last

def generate_unique_email(first, last, conn):
    """Generate a unique email based on first and last name with random 2-3 digit suffix"""
    while True:
        # Generate random 2-3 digit number
        num_digits = random.choice([2, 3])
        if num_digits == 2:
            rand_num = random.randint(10, 99)
        else:
            rand_num = random.randint(100, 999)
        # Form email: first.last{rand_num}@gmail.com (lowercase)
        email = f"{first.lower()}.{last.lower()}{rand_num}@gmail.com"
        # Check if email exists
        cursor = conn.execute('SELECT 1 FROM users WHERE email = ?', (email,))
        if cursor.fetchone() is None:
            return email
        # else loop again to generate a new random number

def main():
    conn = get_db()
    try:
        # Generate Indian name
        first, last = generate_indian_name()
        name = f"{first} {last}"
        # Generate unique email
        email = generate_unique_email(first, last, conn)
        # Password hash
        password_hash = generate_password_hash('password123')
        # Insert user
        cursor = conn.execute(
            '''INSERT INTO users (name, email, password_hash) VALUES (?, ?, ?)''',
            (name, email, password_hash)
        )
        conn.commit()
        user_id = cursor.lastrowid
        # Fetch the inserted user for confirmation
        user = conn.execute('SELECT id, name, email FROM users WHERE id = ?', (user_id,)).fetchone()
        print(f"id: {user['id']}")
        print(f"name: {user['name']}")
        print(f"email: {user['email']}")
    finally:
        conn.close()

if __name__ == '__main__':
    main()