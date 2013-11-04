from importlib import import_module

from matcha import make_wsgi_app

from uiro.db import initdb
from uiro.static import get_static_app_matching
from uiro.template import setup_lookup


def main(global_conf, root, **settings):
    """ Entry point to create Uiro application.

    Setup all of necessary things:

      * Getting root matching
      * Initializing DB connection
      * Initializing Template Lookups
      * Collecting installed applications
      * Creating apps for serving static files

    and will create/return Uiro application.
    """
    matching = import_module_attribute(settings['uiro.root_matching'])
    apps = [import_module(app_name)
            for app_name in settings['uiro.installed_apps'].split('\n')
            if app_name != '']

    static_matching = get_static_app_matching(apps)
    if static_matching:
        matching = static_matching + matching

    setup_lookup(apps)
    initdb(settings)
    return make_wsgi_app(matching)


def import_module_attribute(path, splitter=':'):
    module_name, attr = path.rsplit(splitter, 1)
    module = import_module(module_name)
    return getattr(module, attr)
