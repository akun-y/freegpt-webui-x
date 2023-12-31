from server.bp import bp
from server.config import get_config
from server.website import Website
from server.backend import Backend_Api
from json import load
from flask import Flask

def app(environ, start_response):
    print("start...")
    # Load configuration from config.json
    
    site_config = get_config.get('site_config')
    url_prefix = get_config.get('url_prefix')

    # Set up the website routes
    site = Website(bp, url_prefix)
    for route in site.routes:
        bp.add_url_rule(
            route,
            view_func=site.routes[route]['function'],
            methods=site.routes[route]['methods'],
        )

    # Set up the backend API routes
    backend_api = Backend_Api(bp, config)
    for route in backend_api.routes:
        bp.add_url_rule(
            route,
            view_func=backend_api.routes[route]['function'],
            methods=backend_api.routes[route]['methods'],
        )

    # Create the app and register the blueprint
    app = Flask(__name__)
    app.register_blueprint(bp, url_prefix=url_prefix)

    # Run the Flask server
    print(f"Running on {site_config['port']}{url_prefix}")
    app.run(**site_config)
    print(f"Closing port {site_config['port']}")

