from server.bp import bp
from server.config import get_config
from server.services import Services_Api
from server.website import Website
from server.backend import Backend_Api
from json import load
from flask import Flask

if __name__ == '__main__':

    # Load configuration from config.json
    site_config = get_config('site_config')
    url_prefix = get_config('url_prefix')

    # Set up the website routes
    site = Website(bp, url_prefix)
    for route in site.routes:
        bp.add_url_rule(
            route,
            view_func=site.routes[route]['function'],
            methods=site.routes[route]['methods'],
        )

    # Set up the backend API routes
    backend_api = Backend_Api(bp, site_config)
    for route in backend_api.routes:
        bp.add_url_rule(
            route,
            view_func=backend_api.routes[route]['function'],
            methods=backend_api.routes[route]['methods'],
        )
    # Set up the services API routes
    services_api = Services_Api(bp, site_config)
    for route in services_api.routes:
        bp.add_url_rule(
            route,
            view_func=services_api.routes[route]['function'],
            methods=services_api.routes[route]['methods'],
        )
        
    # Create the app and register the blueprint
    app = Flask(__name__)
    app.register_blueprint(bp, url_prefix=url_prefix)

    # Run the Flask server
    print(f"Running on {site_config['port']}{url_prefix}")
    if(get_config('debug')):
        app.run(**site_config)
    else :
        from waitress import serve
        serve(app, **site_config)
        print(f"Closing port {site_config['port']}")
