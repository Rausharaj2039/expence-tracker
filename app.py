from flask import Flask, render_template, request
from database.db import get_db, init_db, seed_db
from werkzeug.security import generate_password_hash

app = Flask(__name__)

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


@app.route("/login")
def login():
    return render_template("login.html")


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
    return "Logout — coming in Step 3"


@app.route("/profile")
def profile():
    return "Profile page — coming in Step 4"


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
    app.run(debug=True, port=5001)