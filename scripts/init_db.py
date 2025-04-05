from superset import app, db

def init_db():
    # Create all tables
    db.create_all()

    # Add any initial data or configurations here
    # For example, creating default roles, users, etc.

if __name__ == "__main__":
    app.app_context().push()
    init_db()