import os
from functools import reduce

from matcha import Matching
from webob.static import DirectoryApp


def generate_static_matching(app,
                             directory_serve_app=DirectoryApp):
    """ Creating a matching for WSGI application to serve static files
    for passed app.

    Static files will be collected from directory named 'static'
    under passed application::

        ./blog/static/

    This example is with an application named `blog`.
    URLs for static files in static directory will begin with
    /static/app_name/. so in blog app case, if the directory has
    css/main.css file, the file will be published like this::

         yoursite.com/static/blog/css/main.css

    And you can get this URL by reversing form matching object::

        matching.reverse('blog:static', path=['css', 'main.css'])
    """
    static_dir = os.path.join(os.path.dirname(app.__file__),
                              'static')
    try:
        static_app = directory_serve_app(static_dir, index_page='')
    except OSError:
        return None
    static_pattern = '/static/{app.__name__}/*path'.format(app=app)
    static_name = '{app.__name__}:static'.format(app=app)
    return Matching(static_pattern, static_app, static_name)


def get_static_app_matching(apps):
    """ Returning a matching containing applications to serve static files
    correspond to each passed applications.
    """
    return reduce(lambda a, b: a + b,
                  [generate_static_matching(app)
                   for app in apps if app is not None])
