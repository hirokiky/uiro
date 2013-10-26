from importlib import import_module

from matcha import make_wsgi_app

from uiro.db import initdb
from uiro.static import get_static_app_matching
from uiro.template import setup_lookup


def main(global_conf, root, **settings):
    matching = import_module_attribute(settings['uiro.root_matching'])
    apps = [import_module(app_name)
            for app_name in settings['uiro.installed_apps'].split('\n')
            if app_name != '']
    matching = get_static_app_matching(apps) + matching
    setup_lookup(apps)
    initdb(settings)
    return make_wsgi_app(matching)


def import_module_attribute(path, splitter=':'):
    module_name, attr = path.rsplit(splitter, 1)
    module = import_module(module_name)
    return getattr(module, attr)
