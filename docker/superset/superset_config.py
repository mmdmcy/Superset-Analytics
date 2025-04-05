from superset.config import *

# Database connection settings
SQLALCHEMY_DATABASE_URI = 'postgresql://user:password@db:5432/superset'
SQLALCHEMY_TRACK_MODIFICATIONS = False

# Enable or disable the feature flags
FEATURE_FLAGS = {
    'ALERTS': True,
    'DASHBOARD_CROSS_FILTERS': True,
}

# Set the secret key for session management
SECRET_KEY = 'your_secret_key_here'

# Configure the authentication method
AUTH_TYPE = AUTH_OID

# Set the default role for new users
PUBLIC_ROLE_LIKE = 'Gamma'

# Enable or disable caching
CACHE_DEFAULT_TIMEOUT = 300
CACHE_CONFIG = {
    'CACHE_TYPE': 'RedisCache',
    'CACHE_KEY_PREFIX': 'superset_',
    'CACHE_REDIS_URL': 'redis://redis:6379/0',
}

# Configure the email settings for alerts and notifications
EMAIL_NOTIFICATIONS = True
SMTP_HOST = 'smtp.example.com'
SMTP_STARTTLS = True
SMTP_SSL = False
SMTP_USER = 'your_email@example.com'
SMTP_PASSWORD = 'your_email_password'
SMTP_PORT = 587

# Other configurations can be added as needed
# For example, setting up logging, additional security settings, etc.