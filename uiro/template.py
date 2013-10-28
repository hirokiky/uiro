import os
from mako.lookup import TemplateLookup


_lookups = None


def setup_lookup(apps, lookup_class=TemplateLookup):
    """ Registering template directories of apps to Lookup.

    Lookups will be set up as dictionary, app name
    as key and lookup for this app will be it's value.
    Each lookups is correspond to each template directories of apps._lookups.
    The directory should be named 'templates', and put under app directory.
    """
    global _lookups

    _lookups = {}
    for app in apps:
        app_template_dir = os.path.join(os.path.dirname(app.__file__),
                                        'templates')
        app_lookup = lookup_class(directories=[app_template_dir],
                                  output_encoding='utf-8',
                                  encoding_errors='replace')
        _lookups[app.__name__] = app_lookup


def get_lookups():
    """ Returning the lookups

    The global variable _lookups should not be imported directory
    by another modules. By importing directory, the value will not
    change evenif setup_lookup
    """
    return _lookups


def get_app_template(name):
    """ Getter function of templates for each applications.

    Argument `name` will be interpreted as colon separated, the left value
    means application name, right value means a template name.

        get_app_template('blog:dashboarb.mako')

    It will return a template for dashboard page of `blog` application.
    """
    app_name, template_name = name.split(':')
    return get_lookups()[app_name].get_template(template_name)
