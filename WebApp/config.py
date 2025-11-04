import os

class Config:
    """Base configuration for the Legal Defence Portal."""

    # Secret key for sessions, CSRF protection, etc.
    SECRET_KEY = os.environ.get("SECRET_KEY") or "change-this-secret-before-deployment"

    # Flask environment
    ENV = os.environ.get("FLASK_ENV") or "development"

    # Debug mode — False for production
    DEBUG = ENV == "development"

    # Path settings
    BASE_DIR = os.path.abspath(os.path.dirname(__file__))

    # Example database (update as needed)
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL") or \
        f"sqlite:///{os.path.join(BASE_DIR, 'app.db')}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Security headers
    SESSION_COOKIE_HTTPONLY = True
    REMEMBER_COOKIE_HTTPONLY = True
    SESSION_COOKIE_SAMESITE = "Lax"
    PREFERRED_URL_SCHEME = "https"

    # Application-specific info
    LEGAL_NOTICE = "This service operates within the jurisdiction of England and Wales."

class DevelopmentConfig(Config):
    DEBUG = True

class ProductionConfig(Config):
    DEBUG = False
    TESTING = False

class TestingConfig(Config):
    TESTING = True
    DEBUG = True
