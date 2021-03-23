import os
import sentry_sdk
import werkzeug
from flask import Flask, render_template, request, session, redirect
from sentry_sdk.integrations.flask import FlaskIntegration
from flask_cors import CORS
from flask_migrate import Migrate
from flask_wtf.csrf import CSRFProtect, generate_csrf
from flask_login import LoginManager

from app.models import db
from .config import Config
from .models import *
from .api.user_routes import user_routes
from .api.product_routes import products_routes
from .api.auth_routes import auth_routes

from .seeds import seed_commands

sentry_sdk.init(
    dsn="https://b812df8f0cec461baad56a165c7f8871@o556590.ingest.sentry.io/5687793",
    integrations=[FlaskIntegration()],

    # Set traces_sample_rate to 1.0 to capture 100%
    # of transactions for performance monitoring.
    # We recommend adjusting this value in production.
    traces_sample_rate=1.0
)

app = Flask(__name__)
app.config.from_mapping({
    'SQLALCHEMY_DATABASE_URI': os.environ.get('DATABASE_URL'),
    'SQLALCHEMY_TRACK_MODIFICATIONS': False,
})


login = LoginManager(app)
login.login_view = 'auth.unauthorized'


@login.user_loader
def load_user(id):
    return User.query.get(int(id))

app.cli.add_command(seed_commands)

app.config.from_object(Config)
app.register_blueprint(user_routes, url_prefix='/api/users')
app.register_blueprint(products_routes, url_prefix='/api/products')
app.register_blueprint(auth_routes, url_prefix='/api/auth')
db.init_app(app)
Migrate(app, db)

CORS(app)

@app.before_request
def https_redirect():
    if os.environ.get('FLASK_ENV') == 'production':
        if request.headers.get('X-Forwarded-Proto') == 'http':
            url = request.url.replace('http://', 'https://', 1)
            code = 301
            return redirect(url, code=code)


@app.after_request
def inject_csrf_token(response):
    response.set_cookie('csrf_token',
                        generate_csrf(),
                        secure=True if os.environ.get(
                            'FLASK_ENV') == 'production' else False,
                        samesite='Strict' if os.environ.get(
                            'FLASK_ENV') == 'production' else None,
                        httponly=True)
    return response


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def react_root(path):
    print("path", path)
    if path == 'favicon.ico':
        return app.send_static_file('favicon.ico')
    return app.send_static_file('index.html')


@app.route('/hello')
def home():
    return "<h1>Hello World!</h1>"

@app.route('/test', methods=['POST'])
def tester():
    res = request.get_json()
    print(request.headers)
    print(request.data)
    return res



@app.errorhandler(werkzeug.exceptions.BadRequest)
def handle_bad_request(e):
    return "<h1>BAD REQUEST</h1>", 400

@app.errorhandler(werkzeug.exceptions.NotFound)
def resource_not_found(e):
    return "RESOURCE NOT FOUND", 404
