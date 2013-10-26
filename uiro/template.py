import os
from mako.lookup import TemplateLookup


_lookups = None


def setup_lookup(apps, lookup_class=TemplateLookup):
    global _lookups

    _lookups = {}
    for app in apps:
        app_template_dir = os.path.join(os.path.dirname(app.__file__), 'templates')
        app_lookup = lookup_class(directories=[app_template_dir],
                                  output_encoding='utf-8',
                                  encoding_errors='replace')
        _lookups[app.__name__] = app_lookup


def get_lookups():
    return _lookups


def get_app_template(name):
    """
    get_app_template('blog:base.mako')
    returns a base template for blog application.
    """
    app_name, template_name = name.split(':')
    return get_lookups()[app_name].get_template(template_name)
