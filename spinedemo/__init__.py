from pyramid.config import Configurator
from sqlalchemy import engine_from_config

from spinedemo.models import initialize_sql

def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    engine = engine_from_config(settings, 'sqlalchemy.')
    initialize_sql(engine)
    config = Configurator(settings=settings)
    config.add_static_view('static', 'spinedemo:static', cache_max_age=3600)

    config.include("cornice")
    config.scan("spinedemo.views")

    config.add_route('root', '/')
    config.add_view('spinedemo.views.root', route_name='root', renderer='spinedemo:templates/root.mak')


    return config.make_wsgi_app()

