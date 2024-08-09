from . import app
from .routes import main_routes

app.register_blueprint(main_routes)