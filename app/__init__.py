from flask import Flask

app = Flask(__name__)

# Safe access to environment value with default fallback
env = app.config.get("ENV", "development").lower()

# Apply the correct config based on environment
if env == "production":
    app.config.from_object("config.ProductionConfig")
elif env == "testing":
    app.config.from_object("config.TestingConfig")
else:
    app.config.from_object("config.DevelopmentConfig")

from app import views
