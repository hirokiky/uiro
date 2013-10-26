import os
from functools import reduce

from matcha import Matching
from webob.static import DirectoryApp


def generate_static_matching(app,
                             directory_serve_app=DirectoryApp):
    static_dir = os.path.join(os.path.dirname(app.__file__),
                              'statics')
    try:
        static_app = directory_serve_app(static_dir, index_page='')
    except OSError:
        return None
    static_pattern = '/static/{app.__name__}/*path'.format(app=app)
    static_name = 'static:{app.__name__}'.format(app=app)
    return Matching(static_pattern, static_app, static_name)


def get_static_app_matching(apps):
    return reduce(lambda a, b: a + b,
                  [generate_static_matching(app)
                   for app in apps if app is not None])
