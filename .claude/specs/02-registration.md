Spec: Registration
Overview
This step implements user registration functionality for the Spendly expense tracker. Users will be able to create new accounts by providing their name, email, and password. The registration form will validate input, hash passwords securely using werkzeug, and store user data in the database. This feature is essential as it enables users to access personalized features like expense tracking, which requires user authentication.

Depends on
Step 1: Database setup (users table already created in database/db.py)

Routes
GET /register — displays registration form — public
POST /register — processes registration submission — public

Database changes
No database changes (users table already created in Step 1)

Templates
Create: None
Modify: 
- templates/register.html — already had correct form structure, no changes needed
- templates/login.html — add success message display capability

Files to change
- app.py — add POST /register route handler
- templates/login.html — add success message display
- static/css/style.css — add auth-success CSS class for styling success messages

Files to create
- None

New dependencies
No new dependencies

Rules for implementation
No SQLAlchemy or ORMs
Parameterised queries only
Passwords hashed with werkzeug
Use CSS variables — never hardcode hex values
All templates extend base.html
Definition of done
- User can access registration page at /register
- Registration form accepts name, email, and password inputs
- Form validates that all fields are filled
- Form validates email format
- Form validates password strength (minimum 8 characters)
- Duplicate email registration shows appropriate error message
- Passwords are hashed using werkzeug.security.generate_password_hash before storage
- Successful registration redirects to login page with success message
- Registration form uses CSS variables for styling (no hardcoded hex values)
- Register template extends base.html
- Login template displays success messages
- Success messages styled appropriately with CSS variables