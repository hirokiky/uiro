from importlib import import_module

from matcha import make_wsgi_app


def main(global_conf, root, **settings):
    matching = import_module_attribute(settings['uiro.root_matching'])
    return make_wsgi_app(matching)


def import_module_attribute(path, splitter=':'):
    module_name, attr = path.rsplit(splitter, 1)
    module = import_module(module_name)
    return getattr(module, attr)
