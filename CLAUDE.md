# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Common Commands
- Run the application: `python app.py` (starts on port 5001)
- Install dependencies: `pip install -r requirements.txt`
- Run tests: `pytest`

## Architecture & Structure
- **Framework**: Flask web application.
- **Application Entry**: `app.py` contains the Flask app instance and all route definitions.
- **Database Layer**: The `database/` directory is intended for database connectivity and initialization (e.g., `database/db.py` for `get_db`, `init_db`, and `seed_db`).
- **Frontend**: 
  - `templates/`: HTML templates using Jinja2.
  - `static/`: Static assets (CSS, JS, images).
- **Environment**: The project uses a virtual environment located in `myenv/`.
