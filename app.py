import os
import logging

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect
from sqlalchemy.orm import DeclarativeBase
from werkzeug.middleware.proxy_fix import ProxyFix

# ------------------------------------------------------------------
# Logging
# ------------------------------------------------------------------
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

# ------------------------------------------------------------------
# SQLAlchemy Base
# ------------------------------------------------------------------
class Base(DeclarativeBase):
    pass

db = SQLAlchemy(model_class=Base)

# ------------------------------------------------------------------
# App Factory (simple)
# ------------------------------------------------------------------
app = Flask(__name__, instance_relative_config=True)

# Default config
app.config.update(
    SECRET_KEY=os.environ.get("SESSION_SECRET", "dev-secret-key-change-in-production"),
    SQLALCHEMY_DATABASE_URI=os.environ.get(
        "DATABASE_URL",
        # SQLite database in the instance folder
        "sqlite:///" + os.path.join(app.instance_path, "tasks.db"),
    ),
    SQLALCHEMY_TRACK_MODIFICATIONS=False,
)

# Ensure instance folder exists
try:
    os.makedirs(app.instance_path, exist_ok=True)
except OSError:
    pass

# Reverse proxy support (optional)
app.wsgi_app = ProxyFix(app.wsgi_app, x_proto=1, x_host=1)

# CSRF protection
csrf = CSRFProtect(app)

# Initialize database
db.init_app(app)

with app.app_context():
    # Import models and routes after app/db are ready
    import models  # noqa: F401
    import routes  # noqa: F401

    # Create all tables if they don't exist
    db.create_all()
    logger.info("Database initialized at %s", app.config["SQLALCHEMY_DATABASE_URI"])

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
