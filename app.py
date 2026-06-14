from flask import Flask, render_template, request, session, redirect, url_for
from database.db import get_db, init_db, seed_db
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.secret_key = 'dev-secret-key-change-in-production'  # Change in production!

# Initialize database on startup
with app.app_context():
    init_db()
    seed_db()


# ------------------------------------------------------------------ #
# Routes                                                              #
# ------------------------------------------------------------------ #

@app.route("/")
def landing():
    return render_template("landing.html")


@app.route("/register")
def register():
    return render_template("register.html")


@app.route("/register", methods=["POST"])
def register_post():
    # Get form data
    name = request.form.get("name", "").strip()
    email = request.form.get("email", "").strip()
    password = request.form.get("password", "")

    # Validation
    error = None
    if not name:
        error = "Name is required."
    elif not email:
        error = "Email is required."
    elif "@" not in email or "." not in email.split("@")[-1]:
        error = "Valid email is required."
    elif not password:
        error = "Password is required."
    elif len(password) < 8:
        error = "Password must be at least 8 characters long."

    if error is None:
        # Check if email already exists
        db = get_db()
        try:
            existing = db.execute(
                "SELECT id FROM users WHERE email = ?", (email,)
            ).fetchone()

            if existing is not None:
                error = "Email already registered."
            else:
                # Hash password and insert user
                password_hash = generate_password_hash(password)
                db.execute(
                    "INSERT INTO users (name, email, password_hash) VALUES (?, ?, ?)",
                    (name, email, password_hash),
                )
                db.commit()
                # Redirect to login page with success message
                return render_template("login.html", success="Registration successful! Please sign in.")
        finally:
            db.close()

    # If validation failed or email exists, show error
    return render_template("register.html", error=error)


@app.route("/login", methods=["GET"])
def login():
    return render_template("login.html")

@app.route("/login", methods=["POST"])
def login_post():
    # Get form data
    email = request.form.get("email", "").strip()
    password = request.form.get("password", "")

    # Validation
    error = None
    if not email:
        error = "Email is required."
    elif not password:
        error = "Password is required."

    if error is None:
        # Check if email exists in database
        db = get_db()
        try:
            user = db.execute(
                "SELECT id, name, password_hash FROM users WHERE email = ?", (email,)
            ).fetchone()

            if user is None:
                error = "Invalid email or password."
            else:
                # Verify password
                if not check_password_hash(user['password_hash'], password):
                    error = "Invalid email or password."
                else:
                    # Login successful, set session
                    session['user_id'] = user['id']
                    session['user_name'] = user['name']  # Store name for navbar
                    db.commit()
                    return redirect(url_for('profile'))
        finally:
            db.close()

    # If validation failed or invalid credentials, show error
    return render_template("login.html", error=error)


@app.route("/terms")
def terms():
    return render_template("terms.html")


@app.route("/privacy")
def privacy():
    return render_template("privacy.html")


# ------------------------------------------------------------------ #
# Placeholder routes — students will implement these                  #
# ------------------------------------------------------------------ #

@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for('landing'))


@app.route("/profile")
def profile():
    # Authentication guard
    if not session.get('user_id'):
        return redirect(url_for('login'))

    # Hardcoded data for the profile page
    user = {
        'name': 'Demo User',
        'email': 'demo@spendly.com',
        'member_since': 'January 2023'
    }

    summary_stats = [
        {'label': 'Total Spent', 'value': '$1,245.50'},
        {'label': 'Transactions', 'value': '42'},
        {'label': 'Top Category', 'value': 'Food'}
    ]

    transactions = [
        {'date': '2023-10-01', 'description': 'Groceries at FreshMart', 'category': 'Food', 'amount': '$56.30'},
        {'date': '2023-09-28', 'description': 'Monthly Bus Pass', 'category': 'Transport', 'amount': '$45.00'},
        {'date': '2023-09-25', 'description': 'Electricity Bill', 'category': 'Bills', 'amount': '$78.90'},
        {'date': '2023-09-20', 'description': 'Movie Night', 'category': 'Entertainment', 'amount': '$22.50'},
        {'date': '2023-09-15', 'description': 'New Laptop', 'category': 'Shopping', 'amount': '$899.99'}
    ]

    category_breakdown = [
        {'category': 'Food', 'total': '$420.00'},
        {'category': 'Transport', 'total': '$180.00'},
        {'category': 'Bills', 'total': '$210.00'},
        {'category': 'Entertainment', 'total': '$90.00'},
        {'category': 'Shopping', 'total': '$345.50'}
    ]

    return render_template(
        "profile.html",
        user=user,
        summary_stats=summary_stats,
        transactions=transactions,
        category_breakdown=category_breakdown
    )


@app.route("/expenses/add")
def add_expense():
    return "Add expense — coming in Step 7"


@app.route("/expenses/<int:id>/edit")
def edit_expense(id):
    return "Edit expense — coming in Step 8"


@app.route("/expenses/<int:id>/delete")
def delete_expense(id):
    return "Delete expense — coming in Step 9"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5001, debug=True)